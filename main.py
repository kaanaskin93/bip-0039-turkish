"""
def sort_bitcoin_words(bitcoin_words):
  sorted_words = sorted(bitcoin_words)
  return sorted_words

with open('your_file.txt', 'r') as file:
    # Read the content of the file and split it into words
    words = file.read().split()

# Print the array of words
print(words)

# Example usage:
bitcoin_2048_word_list = ["word1", "word2", "word2048"]  # Replace ... with the actual words
sorted_bitcoin_words = sort_bitcoin_words(bitcoin_2048_word_list)

print("Original Bitcoin Words:")
print(bitcoin_2048_word_list)

print("\nSorted Bitcoin Words:")
print(sorted_bitcoin_words)

# Read words from input file
with open('english.txt', 'r') as file:
  words = file.read().splitlines()

# Create blank dictionaries and write to output file
output_data = []
for word in words:
  data = {word:""}
  output_data.append(data)

with open('english_turkish.txt', 'w') as output_file:
    for data in output_data:
        json.dump(data, output_file)
        output_file.write('\n')

        

data = []
with open('english_turkish_2.txt') as f:
  for line in f:
    print(line)
    json_data_as_str = f"[{line}]"
    json_data = json.loads(json_data_as_str)
    data.append(json_data)
  print(data)

  
d = {}
with open("v5_turkish_sorted_translationswithoutparanthesis_sameremoved_Xremoved.txt") as f: 
  mylist = f.read().splitlines()
  for line in mylist:
    (key, val) = line.split(': ')
    d[key] = val

# Sorting dictionary
d = sorted([(key, value) for (key, value) in d.items()])

with open('v6_turkishonly_sorted_translationswithoutparanthesis_sameremoved_Xremoved.txt', 'w') as output_file:
  for key, value in d:
    output_file.write(key+'\n')
    
words = []
with open("others.txt") as f: 
  mylist = f.read().splitlines()
  for line in mylist:
    words.append(line)

def findTheDifferentChar(str1,str2):
  diff_count = 0
  if len(str1) == len(str2):
    for i in range(len(str1)):
      if str1[i] != str2[i]:
        diff_count +=1
    return diff_count
  else:
    if len(str1) < len(str2):
      min = str1
      max = str2
    else:
      max = str1
      min = str2
  for i in range(len(min)):
    if min[i] != max[i]:
      diff_count +=1
  diff_count = diff_count +(len(max)-len(min))
  return diff_count

for word in words:
  for word_compared in words:
    diff = findTheDifferentChar(word, word_compared)
    if diff ==1:
      print(diff, word, word_compared)
"""
'''
main_words = []
other_words = []
to_be_added = []
with open("v9_v1others_added.txt") as f: 
  mylist = f.read().splitlines()
  for line in mylist:
    main_words.append(line)

with open("others.txt") as f: 
  mylist = f.read().splitlines()
  for line in mylist:
    other_words.append(line)

  
  for w2 in other_words:
    if w2 in main_words:
      continue
    else:
      to_be_added.append(w2)

  with open('others_tobeadded.txt', 'w') as output_file:
    for w in to_be_added:
      output_file.write(w+'\n')
'''

def TBA_checks(inputTextFile):
  from datetime import datetime

  arr = []
  arr2 = []
  arr3 = []
  arr4 = []
  with open(inputTextFile) as f:
    mylist = f.read().splitlines()
    for line in mylist:
      arr.append(line)

  #remove the same items from the list:
  arr = list(set(arr))

  #remove text that contains Turkish characters, starts with capital and also contains blanks and :
  for text in arr:
    if text[0].isupper():
      continue
    elif 'â' in text or 'ı' in text or 'ğ' in text or 'ü' in text or 'ş' in text or ' ' in text or 'ö' in text or 'ç' in text or ':' in text:
      continue
    else:
      arr2.append(text)

  #remove text with same first 4 letters
  import copy
  arr3 = copy.deepcopy(arr2)
  for text_1 in arr2:
    for text_2 in arr3:
      if text_1[0:4] == text_2[0:4]:
        print(text_1)
      else:
        continue
"""
  #Write the texts that passed into a txt file
  with open(inputTextFile[:-4]+'_output_'+datetime.now().strftime("%H:%M:%S")+'.txt', 'w') as output_file:
    for text_3 in arr4:
      output_file.write(text_3+'\n')
"""
TBA_checks('v2_others.txt')