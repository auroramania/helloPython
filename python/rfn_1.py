# 재귀함수

def factorial(n):
    if n==1:
        return 1
    else :
        return n * factorial(n - 1)
    
factorial(4)

print(factorial(4))