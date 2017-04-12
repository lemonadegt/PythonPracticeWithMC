numbers = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
ten_char = ['', '십', '백', '천', '만', '십', '백', '천', '억', '십', '백', '천', '조']

def changetohanguel(nums):
    numlist = []
    returnvalue = ''

    if len(str(nums)) == 1:
        returnvalue = numbers[nums]
    elif len(str(nums)) > 13:
        returnvalue = '세기 힘들어 그만 요청해...!'
    else:
        numlist.extend(nums)
        counterval = len(str(nums))

        for i in numlist:
            if int(i) == 0:
                returnvalue
            elif int(i) == 1:
                #TODO:: 맨 앞자리가 1인 경우는 어떻게 해야할지 처리 필요
                returnvalue = returnvalue + ten_char[counterval - 1]
            else:
                returnvalue = returnvalue + numbers[int(i)] + ten_char[counterval - 1]

            counterval = counterval - 1

    return returnvalue

obj = str(input("숫자를 입력해 주세요 : "))
#obj = str(200510315)
print(changetohanguel(obj))
