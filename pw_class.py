import getpass

def loginprocess():
    userpw = getpass.getpass("패스워드를 입력해 주세요 : ")

    if ORG_PASSWORD == userpw:
        print("로그인 되었습니다")
    else:
        print("패스워드가 틀렸습니다.")
        errorcount += 1

    if errorcount == 5:
        return False
    else:
        return True

def changepwprocess():
    chkchangepwflag = False

    if loginprocess(originpw):
        print("패스워드를 변경할 수 있습니다.")

        while chkchangepwflag != True:
            newpw = input("새로 변경할 패스워드를 입력해 주세요 : ")
            newpwre = input("새로 변경할 패스워드를 다시 입력해 주세요 : ")
            if originpw == newpw:
                print("기존 패스워드와 동일 합니다.")
            elif newpw != newpwre:
                print("새로 변경할 패스워드가 잘못되었습니다.")
            else:
                print("패스워드 변경이 완료되었습니다.")
                chkchangepwflag = True
        return chkchangepwflag
    else:
        return False

ORG_PASSWORD = "asdjkl123"
CONST_LOGIN = "1"
CONST_CHANGEPW = "2"
CONST_EXIT = "Q"
exitflag = False
errorcount = 0

while exitflag == False:
    selectedmenunum = str(input("원하는 메뉴를 골라주세요\n(1.로그인, 2.암호변경, Q.종료) : ")).upper()

    if selectedmenunum == CONST_LOGIN:
        print("로그인을 선택하였습니다")
        exitflag = loginprocess()
        #exitflag = True
    elif selectedmenunum == CONST_CHANGEPW:
        print("암호변경을 선택하였습니다")
        if changepwprocess() == True:
            print("암호변경을 성공적으로 완료하였습니다")
        else:
            print("암호변경을 실패하였습니다")
        exitflag = True
    elif selectedmenunum == CONST_EXIT:
        print("종료를 선택하였습니다")
        exitflag = True
    else:
        print("잘못된 메뉴를 골랐습니다.")
        errorcount += 1

    if errorcount == 5:
        print("입력을 다섯번 잘못하셨습니다. 종료하겠습니다")
        exitflag = True



#<<< reference >>>
#lower() : 문자열의 모든 글자를 소문자로 변경
#upper() : 문자열의 모든 글자를 대문자로 변경
#capitalize() : 문자열 중 맨 앞글자만 대문자로 하고 나머지는 소문자로 변경
#title() : 문자열 중 단어의 맨 앞글자만 대문자로 하고 나머지는 소문자로 변경
