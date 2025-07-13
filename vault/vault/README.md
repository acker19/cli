# FileVault CLI

## How to Run

```bash
python main.py <command>
```

## Supported Commands
- `upload <filepath>`: Uploads a file
- `list`: Lists all files
- `read <file_id>`: Shows file metadata
- `delete <file_id>`: Deletes a file

## Storage Structure
- Uploaded files: `storage/uploads/`
- Metadata: `storage/metadata.json`
