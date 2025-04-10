import cv2
#  Imports the OpenCV library, which is used for computer vision tasks like reading images, detecting QR codes, etc.

img = cv2.imread('qrcode.png')# Load image

# Initialize the detector
detector = cv2.QRCodeDetector()#Creates a QR code detector object using OpenCV's built-in QRCodeDetector() class.

# Detect and decode
data, bbox, _ = detector.detectAndDecode(img)

'''This scans the image for a QR code, and:
data: the decoded text/message from the QR code (e.g., "HAPPY BIRTHDAY!")
bbox: the bounding box (a list of 4 corner points) where the QR was found
_: (we ignore this one) — it's the straightened QR image which we're not using here

'''

if data:
    print("QR Code Data:", data)
else:
    print("No QR code found")
