def getpw():
    pw = input("패스워드를 입력해주세요 : ")
    return pw

def loginprocess(originpw):
    inputpw = getpw()
    retrycount = 0

    while retrycount < 5:
        if inputpw == originpw:
            print("로그인 되었습니다")
            return True
            break
        else:
            print("패스워드가 틀렸습니다.(" + str(retrycount + 1) + "번)")
            retrycount += 1
            if retrycount == 5:
                print("패스워드 입력을 5번 틀리셨습니다. 접속이 불가능합니다.")
                break
            inputpw = getpw()

def changepwprocess(originpw):
    chkchangepw = False

    if loginprocess(originpw):
        print("패스워드를 변경할 수 있습니다.")

        while chkchangepw != True:
            newpw = input("새로 변경할 패스워드를 입력해 주세요 : ")
            if originpw == newpw:
                print("기존 패스워드와 동일 합니다.")
            else:
                #패스워드 확인 입력 받는 부분 추가
                print("패스워드 변경이 완료되었습니다.")
                chkchangepw = True
    return chkchangepw

def exitprocess():
    print("종료합니다.")
    return True

password = 'asdjkl123'
LOGIN = "1"
CHANGEPW = "2"
EXIT = "q"
chkexitvalue = False

while chkexitvalue != True:
    selectmenu = str(input("원하는 메뉴를 골라주세요(1.로그인, 2.암호변경, q.종료) : "))

    if selectmenu == LOGIN:
        chkexitvalue = loginprocess(password)
    elif selectmenu == CHANGEPW:
        chkexitvalue = changepwprocess(password)
    elif selectmenu == EXIT:
        chkexitvalue = exitprocess()
    else:
        print("잘못된 메뉴를 골랐습니다.")


'''
while password != inputpw:
    inputpw = input("패스워드가 틀렸습니다. 다시 입력해주세요 :")

print("로그인 되었습니다")
'''
