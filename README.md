# pyVideoPlayer
2 X 2 video player

## How this works:
- Opens 4 video files.
- Reads a frame from each one.
- Resizes all frames to the same target size.
- Uses np.hstack and np.vstack to stack them into a 2x2 grid.
- Displays the grid in a single window.
- Loops videos automatically when they end.

## SETUP

Windows : 
```bash
 python -m venv venv
 venv\Scripts\activate
 venv\Scripts\Activate.ps1
 pip install opencv-python numpy

 python '.\import cv2.py'
```
To quit, press **q**
