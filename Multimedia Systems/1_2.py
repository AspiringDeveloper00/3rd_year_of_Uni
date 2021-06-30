from scipy.stats import entropy
import numpy as np
import cv2
import os
import pickle

# ------------------------ Error frames video output / Error frames,vectors encoding in binary ------------------------

# If the script runs in cmd and not in an IDE, this refreshes the completion percent
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Divide the image into macroblocks
def divide_to_macroblocks(k, array):
    macroblocks = []
    for row in range(0, array.shape[0] - k+1, k):
        for col in range(0, array.shape[1] - k+1, k):
            macroblocks.append(array[row:row+k, col:col+k].astype('int32'))
    macroblocks = np.array(macroblocks)
    return macroblocks



# Sub-sample, dividing by 2 each time. The resolution from 720x1280 becomes 180x320 containing 3600 4x4 macroblocks.
# Returns level 2 and 3 ( sampled by 2 and by 4 )
def create_upper_levels(source, target):
    hierimg1 = [source]
    hierimg2 = [target]
    source = np.array(source)
    target = np.array(target)
    # Using the function "hierarchical_division" create 2 new images
    # with lower resolution so we search for the macroblocks matches
    # We go up to level 3
    for i in range(2):
        source = hierarchical_division(source)
        hierimg1.append(source)
        target = hierarchical_division(target)
        hierimg2.append(target)
    return hierimg1, hierimg2

# Sub sampling function
def hierarchical_division(image):
    image = np.array(image)
    height, width = image.shape
    hierarchicalImage = []
    # Sub-sampling dividing each time by 2 both height and width
    for i in range(0, height, 2):
        for j in range(0, width , 2):
            # In case of an even number
            try:
                hierarchicalImage.append(image[i][j])
            except:
                continue
    hierarchicalImage = np.array(hierarchicalImage)
    # Reshape the on column array to our sub-sampled dimensions
    hierarchicalImage = np.reshape(hierarchicalImage, (int(height/2), int(width/2)))
    return hierarchicalImage


# We go from level 3 to level 1 again. If the 3rd 4x4 macroblock with the index 3 had movement
# we now go to a deeper level ( level 3 ---> level 2 ) and check if there is still movement in the 3rd macroblock.
# We continue this for every level and for every macroblock that contained movement in the above level
def move_to_low_levels(movement_blocks,hierimg1,hierimg2):
    search = [8, 16]
    for k in range(len(search)):
        image1 = divide_to_macroblocks(search[k], hierimg1[1-k])
        image2 = divide_to_macroblocks(search[k], hierimg2[1-k])
        no_mevement_blocks = []
        for i in range(len(movement_blocks)):
            if motion_exist(image1[movement_blocks[i]], image2[movement_blocks[i]]):
                continue
            else:
                no_mevement_blocks.append(i)
        tmp = []
        for z in movement_blocks:
            if z not in no_mevement_blocks:
                tmp.append(z)
        movement_blocks = tmp
    return(image1, image2 ,movement_blocks)

# Check if the difference between 2 images is more than 10% then there is motion between these 2 images
def motion_exist(macroblock1, macroblock2):
    diff = np.array(macroblock1 - macroblock2)
    height, width = diff.shape
    res = height*width
    num_of_zeros = res - np.count_nonzero(diff)
    if (num_of_zeros >= 0.9 * res):
        return False
    else:
        return True


# Find which of the neighbour macroblocks has the min sad score
def sad(im1, im2, i):
    block = []
    diff = []
    diff.append(calculate_sad(im2[i], im1[i]))
    block.append(i)
    width = im1.shape[1]

    # Right macroblock
    if i + 1 <= width:
        diff.append(calculate_sad(im2[i], im1[i + 1]))
        block.append(i + 1)

    # Left macroblock
    if i - 1 >= 0:
        diff.append(calculate_sad(im2[i], im1[i - 1]))
        block.append(i - 1)

    # Below macroblock
    if i + width <= width**2:
        diff.append(calculate_sad(im2[i], im1[i + width]))
        block.append(i + width)

    # Above macroblock
    if i - width >= 0:
        diff.append(calculate_sad(im2[i], im1[i - width]))
        block.append(i - width)

    # Diagonal below right
    if i + width + 1 <= width**2:
        diff.append(calculate_sad(im2[i], im1[i + width + 1]))
        block.append(i + width)

    # Diagonal below left
    if i + width - 1 <= width**2:
        diff.append(calculate_sad(im2[i], im1[i + width - 1]))
        block.append(i + width)

    # Diagonal above right
    if i - width + 1 >= 0:
        diff.append(calculate_sad(im2[i], im1[i - width + 1]))
        block.append(i - width)

    # Diagonal above left
    if i - width - 1 >= 0:
        diff.append(calculate_sad(im2[i], im1[i - width - 1]))
        block.append(i - width)

    # Get the index of the neighbour block with the min sad score
    return block[diff.index(min(diff))]

# Calculate the SAD metric because MAD is slower ( more calculations )
def calculate_sad(macro1, macro2):
    sad = 0
    n = macro1.shape[0]
    for i in range(n):
        for j in range(n):
            sad += abs(int(macro1[i, j]) - int(macro2[i, j]))
    return sad


# Rebuild an image from macroblocks
def rebuild_image(height, width, blocks):
    c = 1
    for i in range(height):
        tmp = np.array(blocks[i*(width)])
        for j in range(width-1):
            tmp = np.concatenate((tmp, blocks[c]), axis=1)
            c += 1
        c += 1
        # In the first iteration set the output as the rebuilt row
        if i==0:
            output = tmp
        # Else add the new row to the half-rebuilt image
        else:
            output = np.concatenate((output, tmp), axis=0)
    return output

# A function that measures entropy
def entropy_score(error_frames, base=None):
    value, counts = np.unique(error_frames, return_counts=True)
    return entropy(counts, base=base)

# Import the original video of a walking lion
vid = cv2.VideoCapture('OriginalVideos/lion.mp4')

# Get the number of total frames, the width/height of the video and the frames per second (fps)
frameCount = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
frameWidth = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(vid.get(cv2.CAP_PROP_FPS))

# Set the size of the video as a tuple
size = (frameWidth, frameHeight)


# Create the output file
out = cv2.VideoWriter('OutputVideos/1_2lionerror.avi', cv2.VideoWriter_fourcc(*'MJPG'), fps, size, False)

# A list containing the error frames ( frame(n+1) - frame(n) )
error_frames = []

# A list containing the actual frames
original_frames = []

# A counter for frames
frame_counter = 1

ret, prev_frame = vid.read()
prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
error_frames.append(prev_frame)
codec = []
while vid.isOpened():
    # Read the n-frame
    ret, curr_frame = vid.read()

    # If there are no more frames exit loop
    if not ret:
        break
    # Converting the rgb n-frame to greyscale
    curr_frame = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)

    # Add original n-frame to original_frames
    original_frames.append(np.array(curr_frame, dtype='int8'))

    # Create 2 lists ( 1 for each frame current and previous ), add the according
    # frame and then separate the levels of each frame
    hierimg1, hierimg2 = create_upper_levels(prev_frame, curr_frame)

    # Split into macroblocks the 2 sub-sampled images. 16/2=8 ---> 8/2=4. We sub-sampled until level 3
    macroblocked_image1 = divide_to_macroblocks(4, hierimg1[2])
    macroblocked_image2 = divide_to_macroblocks(4, hierimg2[2])

    # Blocks to be used for the motion compensation
    movement_blocks = []

    # Check which pairs of blocks contain movement
    for i in range(len(macroblocked_image1)):
        if motion_exist(macroblocked_image1[i], macroblocked_image2[i]):
            movement_blocks.append(i)

    # Return lower level macroblocks and blocks that contain movement
    macroblocked_image1, macroblocked_image2, movement_blocks = move_to_low_levels(movement_blocks, hierimg1, hierimg2)

    # Use the sad function to see which neighbour macroblock scores the highest sad number and add their
    # index to the predicted array. Then construct the predicted image
    predicted = []
    for i in range(len(movement_blocks)):
        predicted.append(sad(macroblocked_image1, macroblocked_image2, movement_blocks[i]))
        macroblocked_image1[movement_blocks[i]] = macroblocked_image1[predicted[i]]

    # Add to the codec list the movement blocks and the according predicted ones to be used when decoding
    codec.append([predicted, movement_blocks])

    # Calculate the difference ( error frame ) between the predicted image n+1 and the actual image n and add it
    # to the error_frames array and write it in the output video
    width = int(frameWidth / 16)
    height = int(frameHeight / 16)
    error_frame = rebuild_image(height, width, np.uint8(np.subtract(macroblocked_image2, macroblocked_image1)))
    out.write(error_frame)
    error_frames.append(error_frame.astype('int8'))

    # Print the progress opf encoding
    cls()
    print("Progress: " + str(round(((frame_counter + 1) / frameCount) * 100, 2)) + "% complete")

    # Add to the frame counter and set the current frame as the previous one
    frame_counter = frame_counter + 1
    prev_frame = curr_frame

# Print the entropy of both error frames sequence and the greyscaled original video
print('The error frames sequence was saved in a video named \'1_2lionerror.avi\' with the entropy of '
      + str(entropy_score(error_frames))+'.')
print('The original video named \'lion.mp4\' had an entropy of ' + str(entropy_score(original_frames))+'.')

vid.release()
out.release()
cv2.destroyAllWindows()

# Convert python list to numpy array
error_frames = np.array(error_frames, dtype='int8')

# Create an array named 'specs' of the following video specifications:
# number of frames, video height, video width, frames per second
specs = np.array([frameCount, frameHeight, frameWidth, fps], dtype='int64')

# Save the error frames sequence in  a binary file named 'Encoded1_2.bin'
error_frames.tofile("Encoded1_2.bin")

# Save the specifications of the video ( number of frames, video height, video width, frames per second )
# in a binary file named 'Specs1_2.bin'
specs.tofile("Specs1_2.bin")

vectors = open("Mov_vectors1_2.bin", "wb")
pickle.dump(codec, vectors)
vectors.close()

# -------------------------------------------- Error frames, vectors decoder -------------------------------------------

# Unpack binary file with the error frames sequence
frames = np.fromfile("Encoded1_2.bin",  dtype='int8')

# Unpack binary file with the specifications
specs = np.fromfile("Specs1_2.bin",  dtype='int64')

# Change the shape of the numpy array to a 3D shape with the dimensions = (number of frames, video height, video width )
frames = np.reshape(frames, (specs[0], specs[1], specs[2]))

# Get the movement blocks and the predicted locations for the reconstruction of the p image
vectors = open("Mov_vectors1_2.bin", "rb")
codec = pickle.load(vectors)
vectors.close()

# Create the output file
out = cv2.VideoWriter('OutputVideos/1_2lion.avi', cv2.VideoWriter_fourcc(*'MJPG'), specs[3], (specs[2], specs[1]), False)

for i in range(len(frames)):
    if i == 0:
        out.write(frames[i])
        curr_frame = frames[i]
    else:
        macro = divide_to_macroblocks(16,curr_frame)
        macro2 = divide_to_macroblocks(16, curr_frame)
        for j in range(len(codec[i-1][1])):
            macro2[codec[i-1][1][j]] = macro[codec[i-1][0][j]]
        image = rebuild_image(45, 80, np.uint8(np.add(divide_to_macroblocks(16, frames[i]), macro2)))
        out.write(image)
        curr_frame = image


out.release()
cv2.destroyAllWindows()
