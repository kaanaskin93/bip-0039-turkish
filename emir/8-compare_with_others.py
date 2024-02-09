finals_file_path = "finals.txt"
allseed_file_path = "allseed.txt"

with open(finals_file_path, "r", encoding="utf-8") as finals_file:
    finals_lines = finals_file.readlines()

with open(allseed_file_path, "r", encoding="utf-8") as allseed_file:
    allseed_lines = allseed_file.readlines()

filtered_finals_lines = [line for line in finals_lines if not any(line.startswith(seed[:4]) for seed in allseed_lines)]

with open(finals_file_path, "w", encoding="utf-8") as updated_finals_file:
    updated_finals_file.writelines(filtered_finals_lines)

print("Process completed.")
