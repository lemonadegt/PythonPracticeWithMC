sejeong = int(input("몇 단을 보고 싶어엉? : "))

for loopi in range(1, 10):
    print("%d x %d = %2d" %(loopi, sejeong, (loopi*sejeong)))
print('')

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