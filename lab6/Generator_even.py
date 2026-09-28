def even_number(limit):
    while limit>0:
        if limit%2 == 0:
            yield limit
        limit= limit-1
limit= int(input("enter a num"))
for i in even_number(limit):
    print(i)            