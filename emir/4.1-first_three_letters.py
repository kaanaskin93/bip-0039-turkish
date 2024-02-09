with open("finals.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

unique_lines = []
seen_prefixes = set()

for line in lines:
    prefix = line[:3]
    if prefix not in seen_prefixes:
        unique_lines.append(line)
        seen_prefixes.add(prefix)

with open("finals.txt", "w") as file:
    file.writelines(unique_lines)
