from cli.commands.upload import UploadCommand
from cli.commands.list import ListCommand
from cli.commands.read import ReadCommand
from cli.commands.delete import DeleteCommand

def route_command(args):
    if not args:
        print("No command provided.")
        return

    cmd = args[0]

    if cmd == "upload":
        UploadCommand().execute(args[1:])
    elif cmd == "list":
        ListCommand().execute(args[1:])
    elif cmd == "read":
        ReadCommand().execute(args[1:])
    elif cmd == "delete":
        DeleteCommand().execute(args[1:])
    else:
        print(f"Unknown command: {cmd}")
