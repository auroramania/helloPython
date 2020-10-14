def fn():
    print("fn called")
    
fn()


def exp(x):
    return x ** 2

exp3 = exp(3)
print(exp(3))

def get_fruits():
    return ['오렌지', '사과', '바나나']

print(get_fruits())
print(get_fruits()[1])


def get_name():
    return 'Kent', 'Beck'
name = get_name()

print(get_name()) # tuple로 반환된다.

# name[1] ="aaaa" # tuple은 Read Only list이므로 에러가 생긴다.
# print(get_name())
def full_name(first_name, last_name):
    return first_name + ' ' + last_name

name = get_name()

print(name, full_name('인한', '이')) 

def var_param(a, *vp):
    print(type(vp))
    print(a, len(vp), vp[len(vp)-1])
    
var_param('a', 'b', 'c')  

def default_param(a, b = 'B'):
    print(a,b)
    
default_param('A')
default_param('A', 'C')