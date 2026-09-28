def countdown(num):
    while num>=1:
        yield num
        num=num-1
num=int(input("enter a num"))
for i in countdown(num):
    print(i)        