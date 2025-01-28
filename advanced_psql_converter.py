import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox, simpledialog
import pandas as pd
import csv
import os

class FileConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File to PostgreSQL Format Converter")
        self.root.geometry("600x600")

        # File path and data tracking
        self.file_path = None
        self.dataframe = None

        # GUI Components
        tk.Label(root, text="Step 1: Upload a File (Log/Text/CSV)", font=("Arial", 12)).pack(pady=5)
        tk.Button(root, text="Upload File", command=self.upload_file).pack(pady=5)
        
        tk.Label(root, text="Preview (Top 50 Rows)", font=("Arial", 12)).pack(pady=5)
        self.preview_output = scrolledtext.ScrolledText(root, height=15, width=70)
        self.preview_output.pack(pady=5)
        
        tk.Button(root, text="Modify Columns", command=self.modify_columns).pack(pady=5)
        tk.Button(root, text="Save Converted File", command=self.save_converted_file).pack(pady=5)
        tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

    def upload_file(self):
        # Open file dialog to select a file
        self.file_path = filedialog.askopenfilename(
            filetypes=[("Log/Text/CSV Files", "*.log *.txt *.csv"), ("All Files", "*.*")]
        )
        if self.file_path:
            messagebox.showinfo("File Uploaded", f"Uploaded: {os.path.basename(self.file_path)}")
            self.process_file()
        else:
            messagebox.showerror("Error", "No file selected.")

    def process_file(self):
        try:
            # Guess the delimiter and read the first 50 lines
            with open(self.file_path, 'r') as file:
                first_50_lines = ''.join(file.readlines()[:50])
            
            delimiter = self.guess_delimiter(first_50_lines)
            self.dataframe = pd.read_csv(self.file_path, delimiter=delimiter)

            # Display the first 50 rows
            output_preview = self.dataframe.head(50).to_csv(index=False, quoting=csv.QUOTE_ALL)
            self.preview_output.delete("1.0", "end")
            self.preview_output.insert("1.0", output_preview)
            
            messagebox.showinfo("Preview", "Displayed the first 50 rows. You can now modify columns.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process the file: {e}")

    def modify_columns(self):
        if self.dataframe is None:
            messagebox.showerror("Error", "No file processed yet. Please upload a file first.")
            return
        
        # Show current columns
        current_columns = list(self.dataframe.columns)
        messagebox.showinfo("Columns", f"Current Columns: {', '.join(current_columns)}")

        # Ask user to rename columns
        for col in current_columns:
            new_col = simpledialog.askstring("Rename Column", f"Rename column '{col}' (Leave blank to keep the same):")
            if new_col:
                self.dataframe.rename(columns={col: new_col}, inplace=True)

        # Ask user to remove columns
        remove_cols = simpledialog.askstring(
            "Remove Columns",
            "Enter columns to remove (comma-separated), or leave blank to keep all:"
        )
        if remove_cols:
            remove_cols = [col.strip() for col in remove_cols.split(",")]
            self.dataframe.drop(columns=remove_cols, inplace=True, errors='ignore')

        # Update the preview with modified columns
        output_preview = self.dataframe.head(50).to_csv(index=False, quoting=csv.QUOTE_ALL)
        self.preview_output.delete("1.0", "end")
        self.preview_output.insert("1.0", output_preview)

        messagebox.showinfo("Modification Complete", "Column modifications applied.")

    def save_converted_file(self):
        if self.dataframe is None:
            messagebox.showerror("Error", "No data available to save. Please upload and process a file first.")
            return

        # Ask for output directory and filename
        output_dir = filedialog.askdirectory(title="Select Output Directory")
        if not output_dir:
            messagebox.showerror("Error", "No output directory selected.")
            return

        output_filename = simpledialog.askstring("Output Filename", "Enter the output filename (with .csv extension):")
        if not output_filename.endswith(".csv"):
            messagebox.showerror("Error", "Filename must end with '.csv'.")
            return

        output_path = os.path.join(output_dir, output_filename)
        try:
            self.dataframe.to_csv(output_path, index=False, quoting=csv.QUOTE_ALL)
            messagebox.showinfo("File Saved", f"File successfully saved as {output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save the file: {e}")

    @staticmethod
    def guess_delimiter(sample_data):
        # Guess the delimiter based on the first few lines of the sample data
        delimiters = ['\t', ',', '|', ';']
        first_line = sample_data.split("\n")[0]
        for delimiter in delimiters:
            if delimiter in first_line:
                return delimiter
        raise ValueError("Could not determine the delimiter. Please ensure the file format is correct.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = FileConverterApp(root)
    root.mainloop()
