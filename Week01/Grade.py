# **요구사항**

# - 학생 5명의 점수를 관리
# - 점수에 따라 A / B / C / D 등급 출력
# - 전체 평균 계산
# - 최고점 / 최저점 출력

# 등급 기준

# - A : 90점 이상
# - B : 80점 이상
# - C : 70점 이상
# - D : 그 외

S1 = int(input("학생 1의 점수를 입력하세요: "))
S2 = int(input("학생 2의 점수를 입력하세요: "))
S3 = int(input("학생 3의 점수를 입력하세요: "))
S4 = int(input("학생 4의 점수를 입력하세요: "))
S5 = int(input("학생 5의 점수를 입력하세요: "))
scores = [S1, S2, S3, S4, S5]
print(scores)
print(max(scores))
print(min(scores))
print(sum(scores) / len(scores))
for score in scores:
    if score >= 90:
        print(f"{score}점 - A등급")
    elif score >= 80:
        print(f"{score}점 - B등급")
    elif score >= 70:
        print(f"{score}점 - C등급")
    else:
        print(f"{score}점 - D등급")

