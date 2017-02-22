# odd = 홀수
# even = 짝수

numbers = [9, 56, 75, 31, 18, 19, 3, 4, 6, 7, 8, 2, 13, 56, 79, 23, 44, 56, 67, 87, 88]
oddnum = []
evennum = []

for i in numbers:
    if i % 2 == 1:
        oddnum.append(i)
    else:
        evennum.append(i)

print("Odd numbers :", oddnum)
print("Even numbers :", evennum)
