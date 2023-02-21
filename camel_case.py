x = input("Enter a name: ")
new_name = ""

for i in x:
    if i.isupper():
        i = "_" + i.lower()
    new_name += i

print(new_name)