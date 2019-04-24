import numpy as np
import cv2

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)
        
if __name__ == "__main__":
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_circle)

    while True:
        cv2.imshow('image', img)
        if cv2.waitKey(2) & 0xff == ord('q'):
            break

    cv2.destroyAllWindows()
    pass