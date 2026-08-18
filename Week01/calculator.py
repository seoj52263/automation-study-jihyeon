num1 = int(input("숫자a 입력: "))
num2 = int(input("숫자b 입력: "))
print(f"a+b = {num1+num2}")
print(f"a-b = {num1-num2}")
print(f"a*b = {num1*num2}")
if num2 == 0:
    print("0으로 나눌 수 없습니다")
else:
    print(f"a/b = {num1/num2}")