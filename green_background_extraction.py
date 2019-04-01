import cv2
import numpy as np

# Initializing Video capture
cap = cv2.VideoCapture(0)

BOX_SIZE = 300
BOX_X, BOX_Y = int(cap.get(3) / 8), int(cap.get(4) / 2 - BOX_SIZE // 2)

while True:

    # Reading frames from Video
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # Cropping the image
    cropped_img = frame[BOX_Y:BOX_Y + BOX_SIZE, BOX_X:BOX_X + BOX_SIZE]

    empty_image = np.zeros_like(cropped_img)
    RED, GREEN, BLUE = (2, 1, 0)

    reds = cropped_img[:, :, RED]
    greens = cropped_img[:, :, GREEN]
    blues = cropped_img[:, :, BLUE]

    mask = (greens < 35) | (reds > greens) | (blues > greens)
    result = np.where(mask, 255, 0)

    # Drawing Box in the given coordinates
    cv2.rectangle(frame, (BOX_X, BOX_Y), (BOX_X + BOX_SIZE, BOX_Y + BOX_SIZE), (255, 0, 0), 2)

    # Showing the frame
    cv2.imshow('Sign Language', frame)

    # Exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite('test.JPG', result)
        break

# Releasing Video capture
cap.release()
cv2.destroyAllWindows()