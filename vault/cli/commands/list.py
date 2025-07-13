from services.file_service import FileService

class ListCommand:
    def execute(self, args):
        files = FileService().list_files()
        if not files:
            print("No files found.")
            return
        print("ID         | Name        | Size     | Uploaded At")
        print("-" * 55)
        for f in files:
            size_kb = round(f["size"] / 1024, 2)
            print(f'{f["id"]:<10} | {f["name"]:<12} | {size_kb} KB  | {f["uploaded_at"]}')
