#! /usr/bin/env python3

#main.py
import cv2
import numpy as np

def capture_and_detect_edges():
    """
    Capture a photo from webcam and detect edges using Canny edge detection
    """
    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return
    
    print("Press 'SPACE' to capture a photo and detect edges")
    print("Press 'ESC' to exit")
    
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Could not read frame")
            break
        
        # Display the original frame
        cv2.imshow('Webcam - Press SPACE to capture, ESC to exit', frame)
        
        # Wait for key press
        key = cv2.waitKey(1) & 0xFF
        
        # If space is pressed, capture and process
        if key == ord(' '):
            print("Capturing photo and detecting edges...")
            
            # Convert to grayscale for edge detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Apply Gaussian blur to reduce noise
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)
            
            # Apply Canny edge detection
            edges = cv2.Canny(blurred, 50, 150)
            
            # Display results
            cv2.imshow('Original Photo', frame)
            cv2.imshow('Grayscale', gray)
            cv2.imshow('Edges Detected', edges)
            
            # Save the images
            cv2.imwrite('captured_photo.jpg', frame)
            cv2.imwrite('edges_detected.jpg', edges)
            print("Images saved: 'captured_photo.jpg' and 'edges_detected.jpg'")
            
        # If ESC is pressed, exit
        elif key == 27:
            break
    
    # Release everything when job is finished
    cap.release()
    cv2.destroyAllWindows()

def main():
    print("OpenCV Webcam Edge Detection")
    print("============================")
    capture_and_detect_edges()
    print("============================")

if __name__ == "__main__":
    main()