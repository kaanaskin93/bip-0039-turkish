
# sort the array
def sort(words):
  sorted_words = sorted(words)
  return sorted_words

# write array to file
def writeToFile(arr):
  from datetime import datetime
  filename = datetime.now().strftime("%H:%M:%S")
  with open(filename+'.txt', 'w') as output_file:
    for a in arr:
      output_file.write(a+'\n')
  print('File created: '+ filename)

# Read words from input file and create the array full of those
def readFromFileAndGenerateArray(filename):
  arr = []
  with open(filename ,'r') as file:
    words = file.read().splitlines()
  for word in words:
    arr.append(word)
  return arr

# Remove duplicates from array
def removeDuplicatesInArray(arr):
  return list(set(arr))

# Get the different letter count of 2 words
def getDiffCountOfTwoWords(str1, str2):
  diff_count = 0
  if abs(len(str1) - len(str2))>1:
    diff_count = abs(len(str1) - len(str2))
  if len(str1) == len(str2):
    for i in range(len(str1)):
      if str1[i] != str2[i]:
        diff_count +=1
  elif abs(len(str1) - len(str2))==1:
    if len(str1)>len(str2):
      max = str1
      min = str2
    else:
      max = str2
      min = str1
    for i in range(len(max)):
      if i == len(max):
        diff_count = 1
      if max[i] == min[i]:
        continue
      else:
        if max[i] != min[i]:
          max_v2 = max[0:i]+max[i+1:len(max)]
          if min == max_v2:
            diff_count = 1
          else:
            diff_count = 2
          return diff_count
  return diff_count

# Check the elements in the array
def checkElementsInArray(arr):
  arr2 = []
  for a in arr:
    if len(a)<4:
      print('ERROR. Too short:', a)

    if a in arr2:
      print('ERROR. Duplicate:', a)
    else:
      for a2 in arr2:
        if a[0:4] == a2[0:4]:
          print('ERROR. Words have the same first 4 letters:', a, a2)
        else:
          if getDiffCountOfTwoWords(a,a2)<2:
            print('ERROR. Words are similar:', a, a2)
    arr2.append(a)
    for c in a:
      if c.isupper():
        print('ERROR. Contains capital letter:', a)
        break
    if 'â' in a or 'ı' in a or 'ğ' in a or 'ü' in a or 'ş' in a or ' ' in a or 'ö' in a or 'ç' in a or ':' in a  or '_' in a:
      print('ERROR. Contains a non-english letter or a sign:', a)
