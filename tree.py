import os

"""
Program to print out the contents of a supplied directory

Planning - 
Initial functions setup for program, maybe i should make it a class
Adding simple program and control flow next
"""


# Function for validating directory exists on user drive
def check_path_exists(dir_path: str) -> bool:
    is_path = os.path.exists(dir_path)
    return is_path


# Function
def check_path_is_directory(dir_path: str) -> bool:
    is_dir = os.path.isdir(dir_path)
    return is_dir


# Function to get absolute path, to ensure getting proper directory contents
def get_absolute_path_to_directory(dir_path: str) -> str:
    abs_path = os.path.abspath(dir_path)
    return abs_path


# Function for getting the contents of directory and putting it into a list
def get_directory_contents(dir_path: str) -> list:
    dir_contents = os.listdir(dir_path)
    return dir_contents


# Function for printing the directory contents
def print_directory_contents(dir_contents: list):
    for item in dir_contents:
        print(item)
