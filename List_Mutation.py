

def remove_last(lst):
    if lst: 
        lst.pop() 
        
    return lst

alist = [1, 2, 3, 4, 5]
print("Original list:", alist)
remove_last(alist) 
print("List after removing last element:", alist)
