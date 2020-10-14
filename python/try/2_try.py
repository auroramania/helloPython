## 이름, 나이, 성별을 입력받아, "당신의 이름은 {}, 나이는 {}, 성별은 {}입니다."출력하기

a= input()
b= int(input())
c= input()

print("당신의 이름은 {}, 나이는 {}, 성별은 {}입니다.".format(a,b,c))




#-----------------------------------------------------------------

cmd = input("Input(usage: 이름,나이,성별)>> ")
print(cmd)
cmds = cmd.split(',')

err_mssge = print("정확히 입력해 주세요.")

# 1. 값이 존재여부 체크
if cmd == '':
    print(err_mssge)
    exit()

# 2. ,가 있는지 체크
if ',' not in cmd:
    print(err_mssge)
    exit()
    
# 3. 3개가 있는지
if len(cmds) != 3:
    print(err_mssge)
    exit()
outmsg = "당신의 이름은 {}, 나이는 {}, 성별은 {}입니다."
print(outmsg.format(cmds[0], cmds[1], cmds[2]))z