def double_result(func):
    def wrapper(a, b):
        
        result=func(a,b)
        r1= result*2
        
        
        return r1
    return wrapper
@double_result
def add(a, b):
    
      
    return a+b

# a=int(input("enter num1")) 
# b=int(input("enter num2"))
ds=add(3,4)
print("doubled_sum",ds)
