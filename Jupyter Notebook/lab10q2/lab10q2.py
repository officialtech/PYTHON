
database = dict()
j = 0

while j < 10:
    name = input("Enter your name: ").capitalize()
    age = int(input("Enter your age: "))
    print(10 * "==")
    j+=1
    database[name] = age


print("Here is the database of all Names & ages\n",database)


sort_by_keys = sorted(database.keys())
print("All keys:", sort_by_keys)


sort_by_values = sorted(database.values())
print("All values:", sort_by_values)



def search_in_db(name):
    '''
        You can search any name in dictonary, just call search_in_db function and pass the
        name what you want to search as a parameter
    '''
    for key,value in database.items():
        if str(name).capitalize() in key:
            print("Name :",key, "Age :", value)
            break
    else:
        print("Person not Found!")

