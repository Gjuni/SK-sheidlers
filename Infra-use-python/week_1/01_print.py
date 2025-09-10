name, age = input().strip().split() # strip은 공백 제거, split (공백으로 자른다)

print("\n",type(name))
print(type(age),"\n")

print("name : {}\n age : {}\n".format(name, age))
print(f"name : {name}\n age : {age}")

# print(""" Hello world
# good day commander
# ByeBye world""")