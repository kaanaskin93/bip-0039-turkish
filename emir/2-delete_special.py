import re

def clean_and_overwrite_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    cleaned_lines = []

    for line in lines:
        # Remove lines containing non-English alphabet characters and 'x', 'w', 'q'
        if re.search('[^a-zA-Z\s]', line) or any(char in line for char in ['x', 'w', 'q']):
            continue
        cleaned_lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(cleaned_lines)

# Example usage
file_path = 'finals.txt'
clean_and_overwrite_file(file_path)
