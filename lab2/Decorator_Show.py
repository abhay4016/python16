def show_info(func):

    def wrapper(num):
        print("before the function")
        r=func(num)
        print("after the function")
        return r
    return wrapper
@show_info
def square(num):
    print("during")
    return num**2
num= int(input("enter a num"))
print("the sqare of number is",square(num))           
