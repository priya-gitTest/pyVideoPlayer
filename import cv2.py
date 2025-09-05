import cv2
import numpy as np
import tkinter as tk

# Paths to 4 video files
video_files = [
    "Bristol vid 1.mp4",
    "Methods RSE conference event - Rolling graphic.mp4",
    "video3.mp4",
    "Animated Slide Deck.mp4"
]

# Open 4 video captures
caps = [cv2.VideoCapture(v) for v in video_files]

# Target size for each video tile (smaller before scaling up)
target_width, target_height = 320, 240  

# Detect screen resolution with tkinter
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

# Create a resizable window and maximize it
cv2.namedWindow("Video Wall (2x2)", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Video Wall (2x2)", screen_width, screen_height)

while True:
    frames = []
    for cap in caps:
        ret, frame = cap.read()
        if not ret or frame is None:
            # Restart video if it ends
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = cap.read()
        if frame is None:
            continue
        # Resize each video frame
        frame = cv2.resize(frame, (target_width, target_height))
        frames.append(frame)

    if len(frames) < 4:
        continue  # wait until all 4 are ready

    # Combine frames into 2x2 grid
    top_row = np.hstack((frames[0], frames[1]))
    bottom_row = np.hstack((frames[2], frames[3]))
    grid = np.vstack((top_row, bottom_row))

    # Resize the grid to full screen
    fullscreen_grid = cv2.resize(grid, (screen_width, screen_height))

    # Show grid
    cv2.imshow("Video Wall (2x2)", fullscreen_grid)

    # Break on 'q' or if window is closed
    if (cv2.waitKey(30) & 0xFF == ord('q')) or \
       (cv2.getWindowProperty("Video Wall (2x2)", cv2.WND_PROP_VISIBLE) < 1):
        break

# Release resources
for cap in caps:
    cap.release()

cv2.destroyAllWindows()
