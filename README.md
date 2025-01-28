# File to PostgreSQL Format Converter

# dataconverter.py
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



# Advanced File to PostgreSQL Format Converter
# advanced_psql_converter.py

This advanced Python application provides a graphical interface for converting various file formats (such as log, text, or CSV) into PostgreSQL-compatible CSV formats. The app allows users to upload files, preview the first 50 rows, modify column names and remove unwanted columns, and finally save the converted file. It leverages `tkinter` for the GUI and `pandas` for data manipulation.

## Features:
- **File Upload**: Upload log, text, or CSV files.
- **Preview**: Displays the first 50 rows of the file for preview.
- **Modify Columns**: Rename or remove columns from the dataset.
- **Save Converted File**: Save the processed file to a desired directory with a custom filename.
- **Delimiter Detection**: Automatically detects the delimiter based on the first 50 lines of the file.

## Steps:
1. **Upload a File**: Select a log, text, or CSV file to process.
2. **Preview Data**: View the first 50 rows of the file to verify the data.
3. **Modify Columns**: Rename or remove columns as needed.
4. **Save the Converted File**: Choose an output directory and filename to save the converted file.

## Installation:
1. Clone this repository to your local machine.
2. Install dependencies: `pip install pandas`
3. Run the script to launch the GUI.

## Usage:
1. **Upload File**: Click the "Upload File" button to select a log, text, or CSV file.
2. **Preview the File**: The first 50 rows will be displayed in the preview section.
3. **Modify Columns**: You can rename columns or remove unnecessary ones using the "Modify Columns" button.
4. **Save the File**: Click "Save Converted File" to specify the directory and filename for the converted file.

## Example:
After uploading a file, the app will automatically detect the delimiter and display the first 50 rows. You can modify the columns and save the file in PostgreSQL-compatible CSV format.

---

### Notes:
- The app attempts to guess the delimiter used in the file based on the first 50 lines. Supported delimiters include tab (`\t`), comma (`,`), pipe (`|`), and semicolon (`;`).
- The modified file is saved as a CSV with all values enclosed in double quotes (`"`) for PostgreSQL compatibility.

---

## License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
