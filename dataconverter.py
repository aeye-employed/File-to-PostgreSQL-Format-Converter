import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import pandas as pd
import csv
import os

class FileConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File to PostgreSQL Format Converter")
        self.root.geometry("600x500")
        
        # File path and sample data
        self.file_path = None
        self.sample_data = None

        # GUI Components
        tk.Label(root, text="Step 1: Upload a File (Log/Text/CSV)", font=("Arial", 12)).pack(pady=5)
        tk.Button(root, text="Upload File", command=self.upload_file).pack(pady=5)
        
        tk.Label(root, text="Step 2: Paste Sample Data (10-20 Lines)", font=("Arial", 12)).pack(pady=5)
        self.sample_input = scrolledtext.ScrolledText(root, height=8, width=70)
        self.sample_input.pack(pady=5)
        
        tk.Label(root, text="Step 3: Convert to PostgreSQL Format", font=("Arial", 12)).pack(pady=5)
        tk.Button(root, text="Convert", command=self.convert_file).pack(pady=5)
        
        tk.Label(root, text="Output Preview", font=("Arial", 12)).pack(pady=5)
        self.output_preview = scrolledtext.ScrolledText(root, height=10, width=70)
        self.output_preview.pack(pady=5)
        
    def upload_file(self):
        # Open file dialog to select a file
        self.file_path = filedialog.askopenfilename(
            filetypes=[("Log/Text/CSV Files", "*.log *.txt *.csv"), ("All Files", "*.*")]
        )
        if self.file_path:
            messagebox.showinfo("File Uploaded", f"Uploaded: {os.path.basename(self.file_path)}")
        else:
            messagebox.showerror("Error", "No file selected.")
    
    def convert_file(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please upload a file first.")
            return
        
        # Get the sample data from user input
        self.sample_data = self.sample_input.get("1.0", "end").strip()
        if not self.sample_data:
            messagebox.showerror("Error", "Please paste 10-20 lines of sample data.")
            return
        
        # Guess the delimiter and columns
        try:
            # Use pandas to read the file and parse it based on the sample data
            delimiter = self.guess_delimiter(self.sample_data)
            df = pd.read_csv(self.file_path, delimiter=delimiter)
            
            # Save the output CSV
            output_file = "converted_output.csv"
            df.to_csv(output_file, index=False, quoting=csv.QUOTE_ALL)
            
            # Show the preview in the output section
            with open(output_file, "r") as f:
                self.output_preview.delete("1.0", "end")
                self.output_preview.insert("1.0", f.read())
            
            messagebox.showinfo("Conversion Successful", f"File converted and saved as {output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Conversion failed: {e}")
    
    @staticmethod
    def guess_delimiter(sample_data):
        # Guess the delimiter based on the first few lines of the sample data
        delimiters = ['\t', ',', '|', ';']
        first_line = sample_data.split("\n")[0]
        for delimiter in delimiters:
            if delimiter in first_line:
                return delimiter
        raise ValueError("Could not determine the delimiter. Please ensure the sample data matches the file format.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = FileConverterApp(root)
    root.mainloop()
