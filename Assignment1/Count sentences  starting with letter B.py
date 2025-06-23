text = input("Enter your text: ")

import re
sentences = re.split(r'[.!?]\s*', text.strip())

count = 0
for sentence in sentences:
    if sentence and sentence[0].upper() == 'B':
        count += 1

print("Number of sentences starting with 'B':", count)
