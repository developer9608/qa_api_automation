import os

ENV = os.getenv("TEST_ENV","dev")

BASE_URLS = {
     "dev": "https://jsonplaceholder.typicode.com",
}

BASE_URL = BASE_URLS.get(ENV)

if BASE_URL is None:
    raise ValueError(f"지원하지 않는 환경입니다: {ENV}")