### 5명의 학생 점수를 입력 받고
### 최고 점수, 최저 점수, 90점 넘는 학생 수, 평균 점수를 출력하라ㄴ

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

def over_90(studnet):
    count = 0

    for i in student :
        if(i >= 90) :
            count += 1
    return count

for i in range(LOOP):
    score = int(input())
    student.append(score)

print("가장 높은 점수 : ", high_score(student))
print("가장 낮은 점수 : ",min_score(student))
print("총 점수 : ",total_sum(student))
print("90점을 넘긴 학생 수 : ",over_90(student))

print("""************ReFactoring************""")
print("가장 높은 점수 : ",max(student))
print("가장 낮은 점수 : ",min(student))
print("총 점수 : ",sum(student)/len(student))
print("90점을 넘긴 학생 수 : ",over_90(student))