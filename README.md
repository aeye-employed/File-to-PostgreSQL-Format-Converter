# File to PostgreSQL Format Converter

This Python application provides a simple graphical interface to convert various file formats (such as log, text, or CSV files) into a PostgreSQL-compatible CSV format. The application uses the `tkinter` library for the GUI and `pandas` for handling the file data transformation.

## Features:
- **Upload File**: Select a log, text, or CSV file to convert.
- **Sample Data Input**: Paste 10-20 lines of sample data to help determine the correct delimiter for parsing the file.
- **File Conversion**: Automatically converts the file into a PostgreSQL-compatible CSV format.
- **Output Preview**: Shows a preview of the converted file before saving.

## Steps:
1. Upload a file (log, text, or CSV).
2. Paste 10-20 lines of sample data.
3. Click "Convert" to transform the file into PostgreSQL-compatible CSV format.
4. Preview the output and save the converted file.

## Installation:
1. Clone this repository to your local machine.
2. Install dependencies: `pip install pandas`
3. Run the script to launch the GUI.

## Example:
The application automatically detects the delimiter based on the sample data and converts the file, handling various formats like CSV, tab-separated, pipe-separated, etc.
