name = "ji hwan hyun"

print(name)
print(len(name))
print(name.upper())
print(name[len(name) - 1])
print(name[len(name) - 1] * len(name))
# 과제 19
for LoopI in range(len(name)):
    print(name[LoopI])

mypens = 100
urpens = 90
print("I have", mypens, "pens.")
print("I have "+str(mypens)+" pens.")
print("I have %d pens." %mypens)
print("I have %d pens and you have %d pens." %(mypens, urpens))
print("I have %d%% pens" %mypens)

print(name.count('a'))
print(name.find('s'))
print(name.find('h'))
print(name.index('h'))
print(name.replace(' ', '-'))
print(name.split())
print(name.split('w'))

vowelsum = 0
print("a: %d 개" %name.count('a'))
print("e: %d 개" %name.count('e'))
print("i: %d 개" %name.count('i'))
print("o: %d 개" %name.count('o'))
print("u: %d 개" %name.count('u'))
vowelsum = vowelsum + name.count('a') + name.count('e') + name.count('i') + name.count('o') + name.count('u')
print("모음은 모두 %d 개" %vowelsum)

# 과제 20
alphabet = 'abcdefghijklmnopqrstuvwxyz'
notusealphabet = ""
for LoopJ in range(len(alphabet)):
    if name.find(alphabet[LoopJ]) == -1:
        notusealphabet += alphabet[LoopJ]
print(name)
print("이름에 사용되지 않은 문자는 %s 입니다." %notusealphabet)

# 머나먼 과제
# 가장 많이 사용된 알파벳과 그 개수를 출력하라
kingwangjjangalphabet = ""
kingwangjjangalphabetcount = 0


