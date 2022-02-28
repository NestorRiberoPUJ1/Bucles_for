for x in range(101):
    print(x)

for x in range(5,1001,5):
    print(x)

for x in range(1,101):
    if(x%10==0):
        print("Coding DOJO")
    elif(x%5==0):
        print("Coding")
    else:
        print(x)

whoa=[]
for x in range(0,500001):
    if(x%2!=0):
        whoa.append(x)
print(sum(whoa))

for x in range(0,2018,4):
    print(2018-x)

lowNum=10
highNum=200
mult=3

for x in range(lowNum,highNum):
    if(x%mult==0):
        print(x)

x=[1,2,3]
x+=[4]
print(x)