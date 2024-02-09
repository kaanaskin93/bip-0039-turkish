with open('finals.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

filtered_lines = [line for line in lines if not any(char.isdigit() for char in line)]

with open('finals.txt', 'w', encoding='utf-8') as file:
    file.writelines(filtered_lines)

print("Deleted.")
