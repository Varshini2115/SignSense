
import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 3
dataset_size = 100

# Try opening the camera
cap = cv2.VideoCapture(0)  # Use camera index 0 (you can change it if needed)
if not cap.isOpened():
    print('Error: Camera not opened.')
    exit()

for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print('Collecting data for class {}'.format(j))

    done = False
    while not done:
        ret, frame = cap.read()
        if not ret:
            print('Error: Failed to capture frame.')
            break

        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        
        key = cv2.waitKey(25)
        if key == ord('q'):
            done = True

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print('Error: Failed to capture frame.')
            break

        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(class_dir, '{}.jpg'.format(counter)), frame)

        counter += 1

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
