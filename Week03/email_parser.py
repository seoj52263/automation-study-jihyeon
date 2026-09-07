import json

def read_emails(filename):
    """파일에서 이메일 목록 읽기"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
        # 줄바꿈 및 공백 제거
        emails = [line.strip() for line in lines if line.strip()]
        return emails
    except FileNotFoundError:
        print(f"{filename} 파일을 찾을 수 없습니다")
        return []

def is_valid_email(email):
    """간단한 이메일 형태 확인"""
    if "@" not in email:
        return False
    if "." not in email:
        return False
    return True

def parse_email(email):
    """이메일을 아이디/도메인으로 분리"""
    id_part, domain_part = email.split("@")
    return id_part, domain_part

def analyze_emails(emails):
    """정상/비정상 구분 + 도메인별 개수 계산"""
    valid_emails = []
    invalid_emails = []
    domain_count = {}

    for email in emails:
        if is_valid_email(email):
            valid_emails.append(email)
            id_part, domain_part = parse_email(email)
            if domain_part in domain_count:
                domain_count[domain_part] += 1
            else:
                domain_count[domain_part] = 1
        else:
            invalid_emails.append(email)

    result = {
        "total": len(emails),
        "valid_count": len(valid_emails),
        "invalid_count": len(invalid_emails),
        "valid_emails": valid_emails,
        "invalid_emails": invalid_emails,
        "domain_count": domain_count
    }
    return result

def save_to_json(data, filename):
    """분석 결과를 JSON 파일로 저장"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"{filename}에 저장되었습니다")

def main():
    emails = read_emails("emails.txt")
    if not emails:
        print("처리할 이메일이 없습니다")
        return

    result = analyze_emails(emails)
    print(result)
    save_to_json(result, "parsed_emails.json")

if __name__ == "__main__":
    main()