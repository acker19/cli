from services.file_service import FileService

class DeleteCommand:
    def execute(self, args):
        if not args:
            print("Usage: vault delete <file_id>")
            return
        try:
            FileService().delete_file(args[0])
            print("File deleted successfully!")
        except Exception as e:
            print(f"Error: {e}")
