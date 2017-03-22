import random
import string

org = ''.join(random.sample(string.ascii_letters, len(string.ascii_letters)))
uppercase = ""
lowercase = ""

for i in org:
    if (ord('A') <= ord(i) <= ord('Z')):
        uppercase += i
    if (ord('a') <= ord(i) <= ord('z')):
        lowercase += i

print(org)
print(uppercase)
print(lowercase)
