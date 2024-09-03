import os
from PyPDF2 import PdfReader, PdfWriter
import string

# Define the decryption password (should be the same as used for encryption)
password = "12345"

# Function to decrypt a single PDF file and overwrite it
def decrypt_pdf(filepath, password):
    try:
        pdf_reader = PdfReader(filepath)
        pdf_writer = PdfWriter()

        # Decrypt the PDF
        if pdf_reader.is_encrypted:
            pdf_reader.decrypt(password)
            for page_num in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page_num])

            # Overwrite the original file
            with open(filepath, "wb") as f:
                pdf_writer.write(f)

            # Rename the file to "Decrypted by ZAZ" + original name
            directory, original_filename = os.path.split(filepath)
            new_filename = f"{original_filename}"
            new_filepath = os.path.join(directory, new_filename)
            os.rename(filepath, new_filepath)

            print(f"Decrypted and renamed to {new_filename}")
    except Exception as e:
        print(f"Failed to decrypt {filepath}: {e}")

# Function to search and decrypt all PDFs in the system
def decrypt_all_pdfs(root_dir, password):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".pdf"):
                filepath = os.path.join(dirpath, filename)
                decrypt_pdf(filepath, password)

# Function to get all available drives and start decryption on each
def decrypt_all_drives(password):
    drives = [f"{d}:\\" for d in string.ascii_uppercase if os.path.exists(f"{d}:\\")]
    for drive in drives:
        print(f"Decrypting PDFs in {drive}")
        decrypt_all_pdfs(drive, password)

# Start the decryption process for all drives
decrypt_all_drives(password)
