import cv2

def count_people(image_path):
    # Load the pre-trained SSD model for person detection
    net = cv2.dnn.readNetFromTensorflow("frozen_inference_graph.pb", "ssd_mobilenet_v2_coco.pbtxt")

    # Load the image
    image = cv2.imread(image_path)
    image_height, image_width, _ = image.shape

    # Prepare the image for object detection (resize and normalization)
    blob = cv2.dnn.blobFromImage(image, size=(300, 300), swapRB=True, crop=False)
    net.setInput(blob)

    # Perform object detection
    detections = net.forward()

    # Count the number of detected people
    num_people = 0
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:  # Consider only detections with confidence greater than 50%
            class_id = int(detections[0, 0, i, 1])
            if class_id == 1:  # Check if the detected object is a person
                num_people += 1

    print("Number of people detected in the photo:", num_people)

# Example usage
image_path = "lionel-messi_imago1019567000h.jpg"
count_people(image_path)
