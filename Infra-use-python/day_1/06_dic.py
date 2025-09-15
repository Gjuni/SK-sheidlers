### 카페 메뉴가 존재하고 입력 값으로 현재 잔액, 메뉴를 입력 받고 계산하는 프로그램을 만들어라

menu = { "아아" : 3500, "라떼" : 4000, "버블티" : 4500 }
order_list = { "아아" : 0, "라떼" : 0, "버블티" : 0 }

for i in menu.keys() :
    print(f"메뉴명 : {i}  가격 : {menu[i]}") # index 값에 해당하는 키 값을 가져옴

total_price = int(input("현재 잔액을 입력해주세요 : "))
reoder = True

while(reoder):
    order = input("주문할 메뉴명을 입력해주세요 : ")

    if(order not in menu.keys()):
        print("존재하지 않는 메뉴입니다.")
        continue    

    current_menu_cost = menu[order]

    if(total_price < current_menu_cost):
        print(f"돈이 부족합니다. 잔액 : {total_price}")
        break
    else :
        total_price -= current_menu_cost
        print(f"잔액 : {total_price}")
        
        order_list[order] += 1
        print(f"{order}이 주문이 완료 되었습니다.")
    
    reorder_current = input("재구매 의사가 있습니까? Y/N : ")

    check = True
    while(check) :
        if((reorder_current is "Y") or (reorder_current is "y")):
            reoder = True
            check = False
        elif ((reorder_current is "N") or (reorder_current is "n")):
            reoder = False
            check = False
        else:
            reorder_current = input("Y/N만 입력이 가능합니다. 다시 입력해주세요: ")
            check = True
        

print("주문을 종료합니다.")

for i in order_list.keys():
    print(f"{i} : {order_list[i]}")