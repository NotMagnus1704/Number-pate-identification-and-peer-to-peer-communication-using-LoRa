import cv2
import easyocr
import serial

# Initialize the camera
cap = cv2.VideoCapture(0)  # Use the default camera

# Check if the camera opened successfully
if not cap.isOpened():
    print("Could not open the camera")
    exit()

# Set up serial connection (adjust '/dev/cu.usbmodem101' to match your Arduino's port)
ser = serial.Serial('/dev/cu.usbmodem101', 9600)

# Create reader instance from EasyOCR
reader = easyocr.Reader(['en'])

# Define the ROI (Region of Interest)
roi_width, roi_height = 300, 200
roi_x = int(cap.get(3) / 2 - roi_width / 2)  # Center the ROI
roi_y = int(cap.get(4) / 2 - roi_height / 2)

print("Press 's' to start detection and 'q' to exit...")

try:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Draw the ROI rectangle on the frame
        cv2.rectangle(frame, (roi_x, roi_y), (roi_x + roi_width, roi_y + roi_height), (0, 255, 0), 2)
        cv2.imshow('Frame', frame)

        # Wait for user input
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            print("Starting detection...")

            # Extract the ROI from the frame
            roi_frame = frame[roi_y:roi_y + roi_height, roi_x:roi_x + roi_width]

            # Use EasyOCR to detect text
            results = reader.readtext(roi_frame)

            # Iterate through the results and display the detected text
            for (bbox, text, prob) in results:
                print(f"Detected: {text} with confidence: {prob}")

                # Only send text with confidence above a threshold (e.g., 0.5)
                if prob >= 0.5:
                    ser.write(text.encode())
                    print("Text sent.")
                    break  # Send the first high-confidence result

        elif key == ord('q'):  # Quit the program
            break

finally:
    # When everything is done, release the capture and close serial
    cap.release()
    cv2.destroyAllWindows()
    ser.close()
