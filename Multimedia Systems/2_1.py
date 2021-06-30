import numpy as np
import cv2
import os

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
        for j in range(0, width, 2):
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


# Import the original video of a walking lion
# vid = cv2.VideoCapture('OriginalVideos/ball.mp4')
# vid = cv2.VideoCapture('OriginalVideos/owl.mp4')
vid = cv2.VideoCapture('OriginalVideos/formula.mp4')

# Get the number of total frames, the width/height of the video and the frames per second (fps)
frameCount = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
frameWidth = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(vid.get(cv2.CAP_PROP_FPS))

# Set the size of the video as a tuple
size = (frameWidth, frameHeight)


# Create the output file
# out = cv2.VideoWriter('OutputVideos/2_1ball.avi', cv2.VideoWriter_fourcc(*'MJPG'), fps, size, False)
# out = cv2.VideoWriter('OutputVideos/2_1owl.avi', cv2.VideoWriter_fourcc(*'MJPG'), fps, size, False)
out = cv2.VideoWriter('OutputVideos/2_1formula.avi', cv2.VideoWriter_fourcc(*'MJPG'), fps, size, False)


# A counter for frames
frame_counter = 1

# Set the first image as the background image
ret, background = vid.read()
background = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
while vid.isOpened():
    # Read the n-frame
    ret, curr_frame = vid.read()

    # If there are no more frames exit loop
    if not ret:
        break
    # Converting the rgb n-frame to greyscale
    curr_frame = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)


    # Create 2 lists ( 1 for each frame current and background ), add the according
    # frame and then separate the levels of each frame
    hierimg1, hierimg2 = create_upper_levels(background, curr_frame)

    # Split into macroblocks the 2 sub-sampled images. 16/2=8 ---> 8/2=4. We sub-sampled until level 3
    background = divide_to_macroblocks(4, hierimg1[2])
    macroblocked_image = divide_to_macroblocks(4, hierimg2[2])

    # Blocks to be used for the motion compensation
    movement_blocks = []

    # Check which pairs of blocks contain movement
    for i in range(len(background)):
        if motion_exist(background[i], macroblocked_image[i]):
            movement_blocks.append(i)

    # Return lower level macroblocks and blocks that contain movement
    background, macroblocked_image, movement_blocks = move_to_low_levels(movement_blocks, hierimg1, hierimg2)

    # For each movement block replace the matching one from the background image
    # to the current frame so we can make the moving object disappear
    for i in range(len(movement_blocks)):
        macroblocked_image[movement_blocks[i]] = background[movement_blocks[i]]

    # Rebuild the corrected frame with the replaced macroblocks
    width = int(frameWidth / 16)
    height = int(frameHeight / 16)
    corrected_frame = rebuild_image(height, width, np.uint8(macroblocked_image))
    out.write(corrected_frame)

    cls()
    # Print the progress opf encoding
    print("Progress: " + str(round(((frame_counter + 1) / frameCount) * 100, 2)) + "% complete")

    # Add to the frame counter and set the current frame as the previous one
    frame_counter = frame_counter + 1

    # Rebuild the background for the next iteration (if the camera is stationary)
    background = rebuild_image(height, width, np.uint8(background))

    # Set as background the rebuilt corrected frame (if camera is moving)
    #background = corrected_frame

# print("New video has been created named \"2_1ball.avi\"!")
# print("New video has been created named \"2_1owl.avi\"!")
print("New video has been created named \"2_1formula.avi\"!")
vid.release()
out.release()
cv2.destroyAllWindows()






