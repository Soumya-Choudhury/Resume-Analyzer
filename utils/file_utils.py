import os
from fastapi import UploadFile

def save_file(file: UploadFile, directory: str):
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, file.filename)

    with open(file_path, "wb") as f:
        f.write(file.file.read())   

    return file_path
