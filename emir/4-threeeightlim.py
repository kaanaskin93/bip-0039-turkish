with open('finals.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

filtered_lines = [line for line in lines if len(line.strip()) <= 8 and len(line.strip()) >= 3]

with open('finals.txt', 'w', encoding='utf-8') as file:
    file.writelines(filtered_lines)
