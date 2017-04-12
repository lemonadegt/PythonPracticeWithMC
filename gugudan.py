numbers = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
ten_char = '십'

'''
sejeong = int(input("몇 단을 보고 싶어엉? : "))

for loopi in range(1, 10):
    print("%d x %d = %2d" %(loopi, sejeong, (loopi*sejeong)))
print('')
'''

def changetohanguel(nums):
    numlist = []

    if len(str(nums)) == 1:
        return numbers[nums]
    elif len(str(nums)) == 2:
        returnvalue = ''

        numlist.extend(str(nums))

        returnvalue = numbers[int(numlist[0])] + ten_char + ' ' + numbers[int(numlist[1])]
        return returnvalue
    else:
        return '응?'

for y in range(1,10):
    for x in range(2,6):
        print('%s x %s = %2d' %(x,y,x*y), end='\t')
    print('')
print('')
for y in range(1,10):
    for x in range(6,10):
        print('%s x %s = %2d' %(x,y,x*y), end='\t')
    print('')
print('')

for y in range(1,10):
    for x in range(2,6):
        print('%s x %s = %2d' %(numbers[x],numbers[y],x*y), end='\t')
    print('')
print('')
for y in range(1,10):
    for x in range(6,10):
        print('%s x %s = %2d' %(numbers[x],numbers[y],x*y), end='\t')
    print('')
print('')

for y in range(1,10):
    for x in range(2,6):
        print('%s x %s = %s' %(numbers[x],numbers[y],changetohanguel(x*y)), end='\t')
    print('')
print('')
for y in range(1,10):
    for x in range(6,10):
        print('%s x %s = %s' %(numbers[x],numbers[y],changetohanguel(x*y)), end='\t')
    print('')
print('')
