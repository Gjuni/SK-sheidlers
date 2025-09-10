student = []
LOOP = 5

def high_score(student):
    max_score = student[0]

    index = 1

    for i in range(LOOP-1):
        now_num = student[index]
        index += 1

        if(now_num >= max_score) :
           max_score = now_num

    return max_score

def min_score(student):
    min_score = student[0]

    index = 1

    for i in range(LOOP-1):
        now_num = student[index]
        index += 1

        if(now_num <= min_score) :
           min_score = now_num

    return min_score

def total_sum(student):
    result = 0
    
    for i in student:
        result += i
    
    return result/LOOP

for i in range(LOOP):
    score = int(input())
    student.append(score)

print(high_score(student))
print(min_score(student))
print(total_sum(student))