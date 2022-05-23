def fibonacci(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        x = fibonacci(n-1)
        x.append(sum(x[:-3:-1]))
        return x
x=fibonacci(9)
print(x)
#done
while True:
    text=input("message")
    if(text[0]=='#'):
        continue
    if(text=="done"):
        break
    print(text)