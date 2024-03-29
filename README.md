# Image Similarity Program

The Image Similarity Program is a Python application that allows users to compare pairs of images, classify them as similar or dissimilar, and save the classification results to a CSV file.

## Features

- **Image Comparison:** Display pairs of images for visual comparison.
- **Classification:** Classify image pairs as either similar or dissimilar.
- **Data Logging:** Save classification results to a CSV file.

## Requirements

- Python 3.x
- PIL (Python Imaging Library)
- Tkinter (Python GUI toolkit)

## Installation

1. Clone the repository to your local machine:

    ```bash
    https://github.com/FogadOg/visualMatcher.git
    ```

2. Navigate to the project directory:

    ```bash
    cd visualMatcher
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the `main.py` file:

    ```bash
    python main.py
    ```

2. The program will display pairs of images from the specified directory (`images/` by default).
   
3. Click the "match" button if the images are similar, or click the "miss match" button if they are dissimilar.

4. Classification results will be saved to the specified CSV file (`imageSimilarityDataset.csv` by default).

## Customization

- **Image Directory:** You can specify the directory containing the images by modifying the `folderPath` parameter when creating an instance of the `Gui` class.
  
- **CSV File:** You can specify the name of the CSV file for saving classification results by modifying the `saveFileName` parameter when creating an instance of the `Gui` class.