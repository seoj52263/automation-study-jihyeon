from dotenv import load_dotenv
import os

# .env 파일 내용을 읽어서 환경변수로 등록
load_dotenv()

def get_config():
    login_id = os.getenv("LOGIN_ID")
    password = os.getenv("LOGIN_PASSWORD")
    base_url = os.getenv("BASE_URL")

    # 필수값이 없으면 원인을 알 수 있게 알려주기
    if login_id is None:
        print("LOGIN_ID가 설정되지 않았습니다. .env 파일을 확인하세요")
        return None
    if password is None:
        print("LOGIN_PASSWORD가 설정되지 않았습니다. .env 파일을 확인하세요")
        return None
    if base_url is None:
        print("BASE_URL이 설정되지 않았습니다. .env 파일을 확인하세요")
        return None

    return {
        "login_id": login_id,
        "password": password,
        "base_url": base_url
    }

def main():
    config = get_config()
    if config is None:
        print("환경설정을 불러오지 못했습니다")
        return

    print(f"로그인 ID: {config['login_id']}")
    print(f"접속 URL: {config['base_url']}")
    print("비밀번호: ****** (보안상 화면에 출력하지 않음)")

if __name__ == "__main__":
    main()