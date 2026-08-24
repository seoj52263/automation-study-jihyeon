import string_utils

# 1. 공백 제거 + 소문자 변환
text = "  Hello World  "
print(string_utils.clean_lower(text))

# 2. 이메일 형태 확인
email = "jihyeon@gmail.com"
print(string_utils.is_valid_email(email))

# 3. 이메일 마스킹
print(string_utils.mask_email(email))

# 4. 단어 개수 계산
sentence = "오늘의 날씨는 맑음"
print(string_utils.count_words(sentence))

# 5. 문자열 반전
print(string_utils.reverse_string("hello"))