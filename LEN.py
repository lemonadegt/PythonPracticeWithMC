def LEN(inSTR):
    count = 0
    #return len(str(inSTR))
    for x in inSTR:
        count += 1
    return  count

print(LEN("Hello, Bill. I love Windows."))
