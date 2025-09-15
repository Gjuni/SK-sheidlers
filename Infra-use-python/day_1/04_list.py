list_str = ["사과", "바나나", "오랜지"]
list_num = [1, 2, 3]

print(type(list_str))
print(type(list_num))

# 인프라팀 - 증권 -> ID, 매수, 매도 -> 저장공간 DB
# 윈도우 -> 레지스트리 -> 메모리 정보, 하드웨어

## List -> 메모리 위에 정보가 올라감.
## 메모리 안에 특정한 정보로 저장이 된다. 메모리에 저장된 정보를 Index 기반으로 꺼내오게 되는 것

## 운영체제에서 연속적으로 메모리에 할당하게 되는데 
## First Fit , Best Fit, Worst Fit이 존재하는데 이때 외부 내부 단편화가 발생하게 됨
## 내부 단편화의 경우 정해진 블록 기준으로 그 안에서 공간이 남는 현상
    ## 내부 단편화의 경우 Fragmentation을 통해 해결할 수 있음.
## 외부 단편화의 경우 전체 메모리 크기에서 메모리가 남게 되는 현상
    ## 해결할 순 없음. 반드시 외부 단편화는 생기지만 Compaction을 통해 메모리 사용을 최적화 할 수 있다.
        ## 다만 실행되는 프로그램의 주소는 변경이 되게 된다.

for list_value in list_str:
    print(f"과일 : {list_value}")

# index(i)값과 value(fruit)값을 가져온다.
for i, fruit in enumerate(list_str):
    print(f"{i+1}번째 Value는 {fruit}입니다.")
