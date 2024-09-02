import os
from bbpy.scanner import scan_bbtools

# Generate commands.py if it doesn't exist
if not os.path.exists(os.path.join(os.path.dirname(__file__), "commands.py")):
    scan_bbtools()

# Import all functions from commands
from bbpy.commands import *