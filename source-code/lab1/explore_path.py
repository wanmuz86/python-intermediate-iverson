import sys

# List of directories Python searches

# Current script directory first

# Standard library locations

# Site-packages for external modules

# Accessible via sys.path

for path in sys.path:
    print(path)