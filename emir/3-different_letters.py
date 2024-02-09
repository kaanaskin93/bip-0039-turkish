def different_letters(word1, word2):
    diff_count = sum(a != b for a, b in zip(word1, word2))
    return diff_count >= 2

def filter_words(word_list):
    if not word_list:
        return []  
    
    new_list = [word_list[0]]
    
    for word in word_list[1:]:
        if all(different_letters(word, prev_word) for prev_word in new_list):
            new_list.append(word)
    
    return new_list

def read_list_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        word_list = file.read().splitlines()
    return word_list

def write_list_to_file(word_list, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(word_list))

file_path = 'finals.txt'
word_list = read_list_from_file(file_path)
filtered_list = filter_words(word_list)
write_list_to_file(filtered_list, file_path)

print("Deleted.")
