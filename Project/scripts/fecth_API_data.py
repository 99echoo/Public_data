import requests
import json
import csv
import os
from dotenv import load_dotenv


def fetch_policy_data(csv_file_path):

    # .env 파일에서 환경 변수 로드
    # 지정된 경로에서 .env 파일 로드
    dotenv_path = 'C:/Users/kdh20/Desktop/Public_data/Project/API_key/여성가족부_key.env'
    load_dotenv(dotenv_path=dotenv_path)
    service_key = os.getenv('SERVICE_KEY')

    if not service_key:
        raise ValueError("SERVICE_KEY가 설정되지 않았습니다. .env 파일을 확인하세요.")


    # API 요청 기본 정보
    url = 'http://apis.data.go.kr/1383000/policy/subjectList'
    api_types = ['youApi', 'equApi', 'famApi', 'proApi', 'othApi']  # 사용할 apiType 목록

    # CSV 파일 오픈 및 헤더 작성
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['담당자 이름', '부서명', '제목', '등록일', '전화번호', '조회수', 'URL'])

        # 각 API 타입과 페이지에 대해 반복
        for api_type in api_types:
            params = {
                'serviceKey' : service_key,
                'type' : 'json',
                'numOFRows' : '10',
                'apiType' : api_type
            }
            for page in range(1, 100):
                params['pageNo'] = page
                try:
                    response = requests.get(url, params=params)
                    response.raise_for_status()  # 요청 실패 시 예외 발생
                    json_data = response.json()
                    items = json_data['body'][0]['items']['item']

                    # 각 항목별 데이터를 CSV 파일에 추가
                    for item in items:
                        writer.writerow([
                            item.get('chrgrNm', ''),
                            item.get('deptNm', ''),
                            item.get('title', ''),
                            item.get('regDt', ''),
                            item.get('telNo', ''),
                            item.get('inqCnt', ''),
                            item.get('url', '')
                        ])
                except (requests.RequestException, ValueError) as e:
                    print(f"페이지 {page} 처리 중 오류 발생: {e}")

    print(f"CSV 파일이 저장된 위치: {csv_file_path}")

# 함수 호출 예시
csv_file_path = "C:/Users/kdh20/Desktop/Public_data/Project/data/여성가족부_정책자료.csv"
fetch_policy_data(csv_file_path)