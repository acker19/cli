import sys
from cli.command_router import route_command

if __name__ == "__main__":
    route_command(sys.argv[1:])
