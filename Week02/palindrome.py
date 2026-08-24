def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]

word = input("문자열을 입력하세요: ")
if is_palindrome(word):
    print("회문입니다")
else:
    print("회문이 아닙니다")