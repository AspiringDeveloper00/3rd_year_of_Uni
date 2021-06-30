This was by far the most challenging task I've ever completed in my 3 years of university. I had to complete the following tasks:

## **Task 1**
Pick a video of your choice having duration 5s - 15s. Assume that Frame 1 is i frame and the next frames are P frames.

i. (1_1.py) Each P frame is inferred without motion compensation from the previous frame. 
Calculate and display the error image sequence and losslessly encode it. Develop the encoder/decoder.

ii. (1_2.py) Develop the frame sequence compression using the motion compensation technique in macroblocks 16x16, search radius k=16, and a macroblocks comparison technique of your choice. 
Calculate and display the error image sequence and losslessly encode it. Develop the encoder/decoder.

## **Task 2**
(2_1.py) Pick a video of your choice having duration 5s - 15s including soft object and camera motion. 
Select the object and remove it using the motion compensation technique. The final video won't have that object.

The original videos are stored in the OriginalVideos folder and the output videos will be created in the OutputVideos folder 
which is currently empty because of storage capacity problems. The encoder creates a binary file of the video ready to be sent over the internet and the decoder decodes that.
Both the encoder and the decoder are in the same file, being executed one after the other for the first 2 sub-tasks.

The documentation is in greek but the python code has a bunch of comments. The original exercise had an extra **task 3** which was a team task completed by all students 
to produce an open-source database containing audio files and the event that was heard in these audios (for example a dog barking, a human speaking or an alarm ringing). 
This open-source database will be added as a link later this year.
