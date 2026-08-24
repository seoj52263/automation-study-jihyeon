
# 앞뒤 공백 제거 + 소문자 변경
def clean_lower(text):
    return text.strip().lower()

# 이메일 확인
def is_valid_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False
# 이메일 마스킹
def mask_email(email):
    if not is_valid_email(email):
        return "유효하지 않은 이메일입니다"
    
    id_part, domain_part = email.split("@")
    if len(id_part) <= 2:
        masked = id_part[0] + "*"
    else:
        masked = id_part[:2] + "*" * (len(id_part) - 2)

    return masked + "@" + domain_part

# 문장 단어 수 (공백으로 세기 > 갯수)
def count_words(sentence):
    words = sentence.split()
    return len(words)
# 문자열 반대로
def reverse_string(text):
    return text[::-1]