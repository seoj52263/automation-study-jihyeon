data = []

while True:
    print("\n1. 데이터 추가")
    print("2. 데이터 조회")
    print("3. 종료")
    choice = input("메뉴를 선택하세요: ")
    
    if choice == "1":
        item = input("추가할 데이터를 입력하세요: ")
        data.append(item)
        print("추가되었습니다")
    elif choice == "2":
        print(data)
    elif choice == "3":
        print("프로그램을 종료합니다")
        break
    else:
        print("잘못된 입력입니다")