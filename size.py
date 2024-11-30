import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
import webbrowser


def get_large_files(directory, size_limit_gb=1):
    """Get a list of files larger than the given size limit (in GB)."""
    size_limit_bytes = size_limit_gb * 1024**3
    return [
        (os.path.join(root, file), os.path.getsize(os.path.join(root, file)) / 1024**3)
        for root, _, files in os.walk(directory)
        for file in files
        if os.path.getsize(os.path.join(root, file)) > size_limit_bytes
    ]


def create_pdf(large_files, pdf_path):
    """Create a PDF report of large files."""
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
            c.drawString(30, height - 40, f"Total large files: {len(large_files)}")
            y = height - 100
        c.setFont("Helvetica", 10)
        c.drawString(30, y, f"{path}: {size:.2f} GB")
        y -= 15

    c.save()
    return pdf_path


def select_directory():
    """Open a dialog to select a directory."""
    directory = filedialog.askdirectory(title="Select Directory to Scan")
    if directory:
        large_files = get_large_files(directory)
        if large_files:
            result_label.config(
                text=f"Found {len(large_files)} files larger than 1GB."
            )
            save_button.config(state=tk.NORMAL)
            global current_large_files
            current_large_files = large_files
        else:
            result_label.config(text="No files larger than 1GB found.")
            save_button.config(state=tk.DISABLED)


def save_report():
    """Save the report as a PDF."""
    pdf_path = filedialog.asksaveasfilename(
        defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], title="Save Report As"
    )
    if pdf_path:
        pdf_file = create_pdf(current_large_files, pdf_path)
        if messagebox.askyesno("Preview PDF", "Do you want to preview the PDF?"):
            webbrowser.open(pdf_file)


# Main GUI setup
root = tk.Tk()
root.title("Large File Finder")
root.geometry("500x300")

# Instructions
label = ttk.Label(
    root, text="Select a directory to scan for files larger than 1GB.", wraplength=450
)
label.pack(pady=10)

# Select directory button
select_button = ttk.Button(root, text="Select Directory", command=select_directory)
select_button.pack(pady=10)

# Result label
result_label = ttk.Label(root, text="", wraplength=450, foreground="blue")
result_label.pack(pady=10)

# Save button
save_button = ttk.Button(root, text="Save Report", state=tk.DISABLED, command=save_report)
save_button.pack(pady=10)

# Exit button
exit_button = ttk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=10)

# Global variable to hold large file data
current_large_files = []

# Start the GUI loop
root.mainloop()
