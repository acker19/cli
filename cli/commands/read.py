from services.file_service import FileService

class ReadCommand:
    def execute(self, args):
        if not args:
            print("Usage: vault read <file_id>")
            return
        try:
            file = FileService().get_file(args[0])
            print(f"Filename: {file['name']}")
            print(f"Size: {round(file['size']/1024, 2)} KB")
            print(f"Path: {file['path']}")
            print(f"Uploaded at: {file['uploaded_at']}")
        except Exception as e:
            print(f"Error: {e}")
