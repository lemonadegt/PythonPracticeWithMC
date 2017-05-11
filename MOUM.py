import random
import string

vowel = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
vowelCounter = 0

# sampleText = ''.join(random.sample(string.ascii_letters, len(string.ascii_letters)))
sampleText = "Hello, Bill. I love Windows."

for i in range(len(str(sampleText))):
    if sampleText[i] in vowel:
        vowelCounter += 1

print('모음은 ' + str(vowelCounter) + '개 있습니다.')


