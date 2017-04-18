#01
ps = ["hello", 3.0, 5, [10, 20]]

print(ps[3][1])



#Q2
birds = ['vulture', 'eagle', 'swallow', 'duck', 'sparrow']
'''
#if birds.count('sparrow') == 1:
if birds.count('sparrow'):
    print('OK')
else
    print('ZZZ')
'''
chkFlag = False
for i in birds:
    if 'sparrow' == i:
        chkFlag = True

if chkFlag:
    print('OK')
else:
    print('ZZZ')



#03
cities = ['Seoul', 'Busan', 'Jeju', 'Sejong', 'Suwon']

for i in cities:
    print('%s is a city' %i)



#04
birds = ['vulture', 'eagle', 'swallow', 'duck', 'sparrow']

usrinput = input('Enter a bird: ')

if usrinput in birds:
    print(usrinput + ' is a bird.')
else:
    print(usrinput + ' is NOT a bird.')



#05
import random

youserLotto = [1,11,22,33,44,45]
lottoORG = []
for i in range(6):
    lottoORG.append(random.randint(1,45))
lottoORG.sort()

print('Lotto numbers are %s' %lottoORG)
print('Your numbers are %s' %youserLotto)
if lottoORG == youserLotto:
    print('You won the Lotto!')
