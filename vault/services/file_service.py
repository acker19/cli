import uuid
import json
import os
from pathlib import Path
from datetime import datetime

class FileService:
    METADATA_FILE = Path("storage/metadata.json")
    UPLOAD_DIR = Path("storage/uploads/")

    def __init__(self):
        self.METADATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        self.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    def load_metadata(self):
        if not self.METADATA_FILE.exists():
            return []
        with open(self.METADATA_FILE, "r") as f:
            return json.load(f)

    def save_metadata(self, data):
        with open(self.METADATA_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def upload_file(self, filepath):
        path = Path(filepath)
        if not path.exists():
            raise FileNotFoundError("File does not exist.")

        file_id = str(uuid.uuid4())[:8]
        dest = self.UPLOAD_DIR / path.name
        with open(path, "rb") as src, open(dest, "wb") as dst:
            dst.write(src.read())

        metadata = self.load_metadata()
        metadata.append({
            "id": file_id,
            "name": path.name,
            "size": path.stat().st_size,
            "path": str(dest),
            "uploaded_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        self.save_metadata(metadata)
        return file_id

    def list_files(self):
        return self.load_metadata()

    def get_file(self, file_id):
        for file in self.load_metadata():
            if file["id"] == file_id:
                return file
        raise ValueError("File not found.")

    def delete_file(self, file_id):
        metadata = self.load_metadata()
        updated = []
        deleted = None
        for file in metadata:
            if file["id"] == file_id:
                deleted = file
                continue
            updated.append(file)
        if not deleted:
            raise ValueError("File not found.")
        self.save_metadata(updated)
        os.remove(deleted["path"])
