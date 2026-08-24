def print_times_table(num):
    for i in range(1, 10):
        print(f"{num} x {i} = {num * i}")

n = int(input("몇 단을 출력할까요? "))
print_times_table(n)