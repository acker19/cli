from services.file_service import FileService

class UploadCommand:
    def execute(self, args):
        if not args:
            print("Usage: vault upload <filepath>")
            return
        try:
            file_id = FileService().upload_file(args[0])
            print(f"File uploaded successfully! ID: {file_id}")
        except Exception as e:
            print(f"Error: {e}")
