import cv2, numpy as np

def draw_circle(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        global ix, iy, radius, drawing, img_
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            # Calculate radius from starting point to current pointer position
            radius = int(np.sqrt((x-ix)**2 + (y-iy)**2))
            # Reset image so previous circles don't remain
            img_ = img.copy()
            # Draw circle
            cv2.circle(img=img_, center=(ix,iy), radius=radius, color=(0,255,0), thickness=5)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        # Calculate radius from starting point to current pointer position
        radius = int(np.sqrt((x-ix)**2 + (y-iy)**2))
        # Draw circle
        cv2.circle(img=img_, center=(ix,iy), radius=radius, color=(0,255,0), thickness=5)

img = cv2.imread('data/dog_backpack.jpg')
img_ = img.copy()
ix, iy, radius, drawing = -1, -1, 0, False
cv2.namedWindow("My Photo")
cv2.setMouseCallback("My Photo", draw_circle)

while True:
    cv2.imshow("My Photo", img_)
    if cv2.waitKey(3) & 0xFF == 27:
        break

cv2.destroyAllWindows()