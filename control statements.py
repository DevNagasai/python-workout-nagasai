# control statements
# while statement
a,b = 0,1
while a< 1000:
    print(a, end = ",")
    a,b = b, a+b

#if statement
x = int(input("Please enter an integer: "))
if x<0:
    x =0
    print('Negative changed to zero')
elif x == 0:
    print('zero')
elif x == 1:
    print('single')
else:
    print('More')

#for statement
words = ['cat', 'windows', 'defenestrate']    
for w in words:
    print(w, len(w))

#Range function in for statemetn

for i in range(5):
    print(i)

range(5,10)
range(0,10,3)
range(-10,-100,-30)

a = ['Mary','had', 'a', 'little','lamb']
for i in range(len(a)):
    print(i,a[i])

print(range(10))

sum(range(4))

list(range(4))

for n in range(2,10):
    for x in range(2,n):
        if n%x ==0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n,'is a prime number')

#pass statements
while True:
    pass

class MyEmptyClass:
    pass

def initlog(*args):
    pass

#fibonacci program
def fib(n):
    a,b = 0,1
    while a<n:
        a,b = b, a+b
    print()

#fibonacci program using a list
def fibl(n):
    result = []
    a,b = 0,1
    while a<n:
        result.append(a)
        a,b = b, a+b
    return result 

    