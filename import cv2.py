import cv2
import numpy as np

# Paths to 4 video files
video_files = [
    "video1.mp4",
    "video2.mp4",
    "video3.mp4",
    "video4.mp4"
]

# Open 4 video captures
caps = [cv2.VideoCapture(v) for v in video_files]

# Get width & height from the first video (resize all to match)
width = int(caps[0].get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(caps[0].get(cv2.CAP_PROP_FRAME_HEIGHT))

# Desired output size for each video in the grid
target_width, target_height = 320, 240  # change as needed

while True:
    frames = []
    for cap in caps:
        ret, frame = cap.read()
        if not ret:
            # Loop video if it ends
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = cap.read()
        # Resize each video frame
        frame = cv2.resize(frame, (target_width, target_height))
        frames.append(frame)

    # Combine frames into 2x2 grid
    top_row = np.hstack((frames[0], frames[1]))
    bottom_row = np.hstack((frames[2], frames[3]))
    grid = np.vstack((top_row, bottom_row))

    # Show grid
    cv2.imshow("Video Wall (2x2)", grid)

    # Break on 'q'
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release resources
for cap in caps:
    cap.release()
cv2.destroyAllWindows()
