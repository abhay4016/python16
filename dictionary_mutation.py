    


def add_entry(d):
    d["new_key"] = "new_value"
    print("Inside add_entry:", d)

def reassign_dict(d):
    d = {"completely_new_key": 42}
    print("Inside reassign_dict:", d)


my_dict = {"original_key": "original_value"}
print("Before add_entry:", my_dict)
add_entry(my_dict)
print("After add_entry:", my_dict)
