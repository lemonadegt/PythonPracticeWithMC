import random
import string

fifty = ''
for i in range(50):
    rchar = random.randint(ord('A'), ord('z'))
    while 91 <= rchar <= 96:
        rchar = random.randint(ord('A'), ord('z'))
    fifty += chr(rchar)

print('생성된 문자열 : %s' %fifty)
print('이 문자열의 길의', len(fifty))

#a = string.ascii_letters
#random.choice(a)

fifty = ''
chars = string.ascii_letters
for i in range(50):
    fifty += random.choice(chars)

print('생성된 문자열 : %s' %fifty)
print('이 문자열의 길의', len(fifty))