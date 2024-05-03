import cv2

def count_people(image_path):
    # Load pre-trained pedestrian detection model
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # Load image
    image = cv2.imread(image_path)

    # Detect people in the image
    (rects, _) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)

    # Draw bounding boxes around detected people
    for (x, y, w, h) in rects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the image with bounding boxes
    cv2.imshow("People Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Count the number of people detected
    num_people = len(rects)
    return num_people

# Path to the image
image_path = "three-people-a-man-and-two-women-taking-selfies-in-the-park-MINF04126.jpg"

# Count people in the image
num_people = count_people(image_path)
print("Number of people in the image:", num_people)
