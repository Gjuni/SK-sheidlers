## 1 ~ 100까지의 숫자 맞추기 게임

# 조건
## 2명의 Player게임에 참가
## Player-1 : 문제를 내는 역할 (Random.number 생성)
## Player-2 : 문제를 맞추는 사용자 (input 영역)

# 로직
## 정답보다 높은지, 낮은지 아니면 정확한지 알려줌.
## 숫자를 맞힐 때까지 이 과정을 반복함.

# range of input
## 1 ~ 100

import random

ran_number = random.randint(1, 100)

check = True

while(check) :
    guess_num = int(input("숫자를 예측해주세요 (1 ~ 100) : "))

    if((guess_num > 100) or (guess_num < 1)) :
        print("숫자는 1 ~ 100 사이의 값입니다. 다시 입력해주세요.")
    elif(guess_num > ran_number):
        print("숫자가 큽니다.")
    elif(guess_num < ran_number):
        print("숫자가 작습니다.")
    else:
        print(f"정답을 맞췃습니다! 정답은 '{ran_number}' 였습니다.")
        check = False