readFile = open('04_file.txt', 'r', encoding='utf-8')

content = readFile.read()
print(f"{content}\n")



with open('04_file.txt', 'r', encoding='utf-8') as file:
    content = file.readline()
    print(f"readLine : {content}")

with open('04_file.txt', 'r', encoding='utf-8') as file:
    content2 = file.readlines()
    print(f"readLines : {content2}")