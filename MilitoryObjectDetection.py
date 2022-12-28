import cv2

# Load the Haar cascade classifier for detecting military objects and personnel
cascade_classifier = cv2.CascadeClassifier('military_cascade.xml')

# Read the input image or video stream
image = cv2.imread('input.jpg')
# or
video_capture = cv2.VideoCapture(0)

while True:
  # If using a video stream, grab the next frame
  if video_capture:
    success, image = video_capture.read()
    if not success:
      break

  # Convert the image to grayscale
  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Detect military objects and personnel in the image
  objects = cascade_classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

  # Draw a bounding box around the detected objects
  for (x, y, w, h) in objects:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)

  # Display the image with the detected objects
  cv2.imshow('Military Detection', image)

  # If using a video stream, wait for the 'q' key to be pressed before exiting
  if video_capture:
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

# Release the video capture object and close all windows
if video_capture:
  video_capture.release()
cv2.destroyAllWindows()
