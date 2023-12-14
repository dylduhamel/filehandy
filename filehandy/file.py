import os
import json
import csv

def read_lines(filepath: str) -> list[str]:
    """
    Reads lines from a file and returns them as a list of strings.
    The file type is determined by the file extension.
    """
    # Determine the file extension
    _, file_extension = os.path.splitext(filepath)

    # Define file type to extension mapping
    file_type_to_extension = {
        '.txt': 'text',
        '.csv': 'csv',
        '.json': 'json',
    }

    file_type = file_type_to_extension.get(file_extension, 'text')

    lines = []

    if file_type == 'text':
        with open(filepath, 'r') as file:
            lines = file.readlines()

    elif file_type == 'csv':
        with open(filepath, 'r') as file:
            csv_reader = csv.reader(file)
            lines = [','.join(row) for row in csv_reader]

    elif file_type == 'json':
        with open(filepath, 'r') as file:
            # Assuming the JSON file contains an array of strings
            data = json.load(file)
            if isinstance(data, list) and all(isinstance(item, str) for item in data):
                lines = data
            else:
                raise ValueError("JSON file does not contain an array of strings.")

    else:
        raise ValueError(f"Unsupported file type: {file_extension}")

    return lines