# 두 수를 받아, 사칙연산을 수행하는 함수를 만들어 보세요.

## 
def plus(a, c):
    return a + c

def minus(a, c):
    return a - c

def mul(a, c):
    return a * c

def div(a, c):
    return a / c

def input_calc():
    cmd = input("사칙연산 계산기 >> ")

    cmds = cmd.split(' ')

    a,b,c = cmds

    a,c = int(cmds[0]), int(cmds[2])

    if b == '+':
        r = plus(a, c)
    elif b == '-':
        r = minus(a, c)
    elif b == '*':
        r = mul(a, c)
    else:
        r = div(a, c)
        
    if b in '+-*':
        print("Answer is {:d}".format(r))
    else :
        print("Answer is {:.3f}".format(r))

while (True):
    input_calc()