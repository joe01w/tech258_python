
import os

# Directory
directory = "test_dir"

# Parent directory
parent_directory = "C:/Users/JW PC/Desktop/Tech_258/github"

# Path
path = os.path.join(parent_directory, directory)

# Create dir
os.mkdir(path)