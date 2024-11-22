import os
import tkinter as tk
from tkinter import filedialog, messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
import webbrowser

def get_large_files(directory, size_limit_gb=1):
   
    size_limit_bytes = size_limit_gb * 1024**3
    return [
        (os.path.join(root, file), os.path.getsize(os.path.join(root, file)) / 1024**3)
        for root, _, files in os.walk(directory)
        for file in files
        if os.path.getsize(os.path.join(root, file)) > size_limit_bytes
    ]

def create_pdf(large_files, pdf_path):
 
    c = canvas.Canvas(pdf_path, pagesize=landscape(A4))
    width, height = landscape(A4)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(30, height - 40, "Files Larger Than 1GB Report")
    c.setFont("Helvetica", 12)
    c.drawString(30, height - 60, f"Total large files: {len(large_files)}")

    y = height - 100
    for path, size in large_files:
        if y < 40:
            c.showPage()
            y = height - 40
            c.setFont("Helvetica-Bold", 14)
            c.drawString(30, height - 40, "Files Larger Than 1GB Report")
            c.setFont("Helvetica", 12)
            c.drawString(30, height - 60, f"Total large files: {len(large_files)}")
            y = height - 100
        c.setFont("Helvetica", 10)
        c.drawString(30, y, f"{path}: {size:.2f} GB")
        y -= 15

    c.save()
    return pdf_path

# Main program
root = tk.Tk()
root.withdraw()

directory = filedialog.askdirectory(title="Select Directory to Scan")

if directory:
    large_files = get_large_files(directory)
    if large_files and messagebox.askyesno("Save PDF", "Save report as PDF?"):
        pdf_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if pdf_path:
            pdf_file = create_pdf(large_files, pdf_path)
            if messagebox.askyesno("Preview PDF", "Preview PDF report?"):
                webbrowser.open(pdf_file)
else:
    print("No directory selected.")
