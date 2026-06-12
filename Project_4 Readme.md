# OCR Text Recognition System

### DecodeLabs Industrial Training — Project 4 | Batch 2026

A simple OCR-based text recognition system that extracts text from images using Python, OpenCV, and Tesseract OCR.

---

## What This Project Does

The system reads an image containing text, preprocesses it for better quality, and extracts the text using Optical Character Recognition (OCR).

---

## Technologies Used

* Python
* OpenCV
* Pytesseract
* Tesseract OCR

---

## How It Works

### Step 1: Load Image

The input image is loaded from the project folder.

### Step 2: Preprocessing

The image is converted to grayscale, blurred to reduce noise, and thresholded to improve text visibility.

### Step 3: OCR Processing

Tesseract OCR scans the processed image and extracts the text.

### Step 4: Output

The recognized text is displayed on the screen.

---

## Required Libraries

```bash
pip install opencv-python
pip install pytesseract
```

---

## Sample Output

Input Image:

```text
WELCOME TO AI
```

Recognized Text:

```text
WELCOME TO AI
```

---

## Applications

* Document Digitization
* Invoice Processing
* Form Recognition
* Text Extraction from Images

---

## Project Structure

```text
OCR_Project.ipynb
sample.jpg
README.md
```

---

## Conclusion

This project demonstrates the basic implementation of Optical Character Recognition (OCR) using image preprocessing and the Tesseract OCR engine to accurately extract text from images.
