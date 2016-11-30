loopCounter = 0

for loopCounter in range(100):
    numberContainer = str(loopCounter)
    lastDigit = numberContainer[len(numberContainer)-1]
    if lastDigit == '9':
        print(loopCounter)

loopCounter = 0

while loopCounter < 100:
    numberContainer = str(loopCounter)
    lastDigit = numberContainer[len(numberContainer)-1]
    if lastDigit == '9':
        print(loopCounter)
    loopCounter += 1
