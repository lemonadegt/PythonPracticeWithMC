inputchar = ord(input('Type a character, plz :'))

if (inputchar >= ord('a')) and (inputchar <= ord('z')):
    print('lower case!')

if (inputchar >= ord('A')) and (inputchar <= ord('Z')):
    print('upper case!')

print('문자 : %c, 10진수 : %d, 16진수 : %x, 8진수 : %o' % (chr(inputchar), inputchar, inputchar, inputchar))

# 대소문자 바꾸기
# 시작 : 문자열이 전부 대문자나 소문자일 때
# 업그레이드 : 문자열에 대소문자가 섞여 있을 때 전부 대소문자로
# 추가 업그레이드 : 문자열에 대소문자가 섞여 있을 때 대문자는 소문자로, 소문자는 대문자로
# 32만큼의 차이

# 문자열 거꾸로 출력
# ABCDEFGHJIKL -> LKIJHGFEDCBA

# 머나먼 과제
# max() / min()
# 현재 수준에서, 즉 10개가 넘는 글자 없음 / 같은 개수인 글자 없음
# 알파벳 문자열을 만든다.
# 글자의 개수들을 요소로 하는 문자열을 생성한다.
# 글자 개수 문자열과 알파벳 문자열을 비교한다.
# cf
# 원래 문자열 : new juan manuel santos
# 가장 많은 글자 : n
# 개수 : 4개
# abcdefghjiklmnopqrstuvwxyz
# 30002000100114100011200000
# 을 비교해서 가장 많은 수의 인덱스를 비교해서 어떤 알파벳인지 찾아내는 것

'''
# 과제 19
name = "ji hwan hyun"
for LoopI in range(len(name)):
    print(name[LoopI])

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
'''

# 16진수 => 0x10 (16) %x
# 8진수 => 0o11 (9) %o
# 2진수 => 0b11 (3)
