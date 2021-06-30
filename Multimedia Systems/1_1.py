import cv2
import numpy as np
from scipy.stats import entropy

# ---------------------------- Error frames video output / Error frames encoding in binary -----------------------------
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
out = cv2.VideoWriter('OutputVideos/1_1lionerror.avi', cv2.VideoWriter_fourcc(*'MJPG'), fps, size, False)

# A list containing the error frames ( frame(n+1) - frame(n) )
error_frames = []

# A list containing the actual frames
original_frames = []

# A function to measure entropy
def entropy_score(error_frames):
  values, counts = np.unique(error_frames, return_counts=True)
  return entropy(counts)

# Read the first frame
ret, prev_frame = vid.read()

# If there is not one (frame) to read then print a message
if not ret:
    print("Something went wrong - can't receive frame.")

# Converting the rgb frame to greyscale
prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

# Add the first frame to the error frames list because we need the first frame to decode later
error_frames.append(np.array(prev_frame,dtype='int8'))

# Add the first frame to the original frames list to measure the original entropy
original_frames.append(np.array(prev_frame,dtype='int8'))



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

    # Calculate ( frame(n+1) - frame(n) )
    image = np.subtract(curr_frame, prev_frame)

    # Write it in the output video
    out.write(image)

    # Add it to the error frames list
    error_frames.append(image.astype('int8'))

    # Set frame(n+1) = frame(n) to use it in the next iteration
    prev_frame = curr_frame

# Print the entropy of both error frames sequence and the greyscaled original video
print('The error frames sequence was saved in a video named \'1_1lionerror.avi\' with the entropy of '
      + str(entropy_score(error_frames))+'.')
print('The original video named \'lion.mp4\' had an entropy of ' + str(entropy_score(original_frames))+'.')

vid.release()
out.release()
cv2.destroyAllWindows()

# Convert python list to numpy array
error_frames = np.array(error_frames)

# Create an array named 'specs' of the following video specifications:
# number of frames, video height, video width, frames per second
specs = np.array([frameCount, frameHeight, frameWidth, fps], dtype='int64')

# Save the error frames sequence in  a binary file named 'Encoded1_1.bin'
error_frames.tofile("Encoded1_1.bin")

# Save the specifications of the video ( number of frames, video height, video width, frames per second )
# in a binary file named 'Specs1_1.bin'
specs.tofile("Specs1_1.bin")


# ------------------------------------------------ Error frames decoder ------------------------------------------------

# Unpack binary file with the error frames sequence
frames = np.fromfile("Encoded1_1.bin",  dtype='int8')

# Unpack binary file with the specifications
specs = np.fromfile("Specs1_1.bin",  dtype='int64')

# Change the shape of the numpy array to a 3D shape with the dimensions = (number of frames, video height, video width )
frames = np.reshape(frames, (specs[0], specs[1], specs[2]))

# Create the output file
out = cv2.VideoWriter('OutputVideos/1_1lion.avi', cv2.VideoWriter_fourcc(*'MJPG'), specs[3], (specs[2], specs[1]), False)

# A flag that indicates the first frame
first_frame_flag = True

# For each frame take the 2D array representing the width and height of the video
for frame in frames:

    # If it's the first frame (which is the original - no error) then write it to file, make it the previous
    # frame and set the flag to false because we found the first frame
    #
    # Else add the previous frame to the current on, write it in the file
    # and set it as the previous frame because we used it
    if first_frame_flag:
        out.write(frame)
        prev_frame = frame
        first_frame_flag = False
    else:
        image=np.add(prev_frame,frame)
        out.write(image)
        prev_frame = image

out.release()
cv2.destroyAllWindows()


