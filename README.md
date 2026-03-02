# Barcode & QR Detector 
### Automated Computer Vision Recognition System

A Python-based computer vision application designed to identify, locate, and decode barcodes and QR codes from image uploads or live camera streams.

---

##  Project Overview 
In modern logistics and retail, manual barcode scanning can be slow and prone to hardware limitations. This project provides a software-based solution that turns any camera-enabled device into a powerful scanner.

**The Workflow:**
* **Image Capture:** The system takes an input from an uploaded file or a real-time Flask-based web interface.
* **Preprocessing:** Using **OpenCV**, images are converted to grayscale and blurred to remove noise that might interfere with scan lines.
* **Localization:** The system detects the bounding box (rectangles) of the barcode within the frame.
* **Decoding:** Using the **Pyzbar/Zbar** library, the localized pixels are translated into alphanumeric strings.
* **Output:** Data is displayed instantly and can be logged for inventory tracking.

---

##  Features
* **Multi-Format Support:** Detects standard barcodes (EAN, UPC, Code 128) and 2D QR codes.
* **Real-Time Scanning:** Optimized for low-latency detection in live video feeds.
* **Robust Preprocessing:** Handles blurry or low-contrast images through automated thresholding.
* **Web Integration:** Includes a **Flask** web portal for easy user interaction.
* **Bulk Processing:** Capability to scan and log multiple barcodes found in a single image.

---

## Technologies Used
* **Language:** Python
* **Computer Vision:** OpenCV
* **Decoding Library:** Pyzbar / ZBar
* **Web Framework:** Flask
* **Data Handling:** NumPy
* **Version Control:** Git

---

