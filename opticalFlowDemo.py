from matplotlib import pyplot as plt
import numpy as np
import math
import cv2

def draw_flow(im,flow,step=5):
    h,w = im.shape[:2]
    y,x = np.mgrid[step/2:h:step,step/2:w:step].reshape(2,-1)
    fx,fy = flow[y,x].T

    # create line endpoints
    lines = np.vstack([x,y,x+fx,y+fy]).T.reshape(-1,2,2)
    lines = np.int32(lines)

    # create image and draw
    vis = cv2.cvtColor(im,cv2.COLOR_GRAY2BGR)
    for (x1,y1),(x2,y2) in lines:
        cv2.line(vis,(x1,y1),(x2,y2),(0,255,0),1)
        cv2.circle(vis,(x1,y1),1,(0,255,0), -1)
    return vis

cap = cv2.VideoCapture(0)

ret, prev_frame = cap.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 7, 1.2, 0)
    prev_gray = gray

    cv2.imshow('Optical flow', draw_flow(gray, flow))
    # cv2.imshow('Optical flow', gray)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
