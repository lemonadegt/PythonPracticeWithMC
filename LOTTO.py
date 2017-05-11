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


# win = [ x for x in you if x in lotto]

