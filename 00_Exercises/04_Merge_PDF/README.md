# Merge PDF Files

A simple Python script that merges multiple PDF files into a single PDF document.

## What it does

This script automatically finds all PDF files in the `pdfs` directory and combines them into one merged PDF file named `Merged-PDF-2023.pdf`.

## Requirements

- Python 3.x
- PyPDF2 library

## Installation

Install the required library:
```bash
pip install PyPDF2
```

## Usage

1. Place all PDF files you want to merge in the `pdfs` folder
2. Run the script:
```bash
python main.py
```
3. The merged PDF will be saved as `Merged-PDF-2023.pdf` in the `pdfs` directory

## Features

- Automatically detects all `.pdf` files in the specified directory
- Merges them in alphabetical order
- Creates a timestamped output file
- Uses PyPDF2 for reliable PDF manipulation

## Note

Make sure you have the `pdfs` directory created and populated with PDF files before running the script. 