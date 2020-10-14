## 1부터 100까지 더하지만 10~20까지는 더하지 않은 누적 합
i,sum = 0,0

while (i>=0):
    i+=1
    if(i > 10 and i < 20):
        continue
    sum += i;
    if (i == 100):
        print("End!! ", sum)
        break
    
lst = ['오렌지', '사과', '배']
dic = {'오렌지':300, '사과':200, '배': 400}

for key in dic:
    print("key=", key, dic[key])
    
print(list(enumerate(lst)))

for i, value in enumerate(lst):
    print("tt=",i,value)
    
for key, element in dic.items():
    print(key, element)