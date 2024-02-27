def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d
    return inner_fun(a, b)

res = outer_fun(5, 10)
print(res)

def display(**kwargs):
    for i in kwargs:
        print(i)

display(emp="Kelly", salary=9000)

def add(a, b):
    return a+5, b+5

result = add(3, 2)
print(result)

x = 0
while x < 10:
    x = x + 1
    print(x)
z = lambda x : x * x



print(z(6))

n=7



c=0



while(n):



if(n>5):



c=c+n-1



n=n-1



else:



break



print(n)



print(c)
