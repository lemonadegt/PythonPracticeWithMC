import os

def find_vowel(obj_string):
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowelCounter = 0

    for i in range(len(str(obj_string))):
        if obj_string[i] in vowel:
            vowelCounter += 1

    return vowelCounter

def get_sample_text_from_dest_file(file_path):
    txtFile = open(file_path, 'r')
    sampleText = txtFile.read()
    txtFile.close()
    return sampleText

def get_file_name(directiry_path):
    tempName = os.path.split(directiry_path)
    return tempName[1]

FILEPATH1 = 'D:\Sources\Github\PythonPracticeWithMC\exfile.txt'
FILEPATH2 = 'D:\Sources\Github\PythonPracticeWithMC\exfile2.txt'

filename = get_file_name(FILEPATH1)
amount = find_vowel(get_sample_text_from_dest_file(FILEPATH1))
print('%s 파일 내의 모음의 숫자는 %s개 입니다.' %(filename, format(amount, ',')))

filename = get_file_name(FILEPATH2)
amount = find_vowel(get_sample_text_from_dest_file(FILEPATH2))
print('%s 파일 내의 모음의 숫자는 %s개 입니다.' %(filename, format(amount, ',')))
