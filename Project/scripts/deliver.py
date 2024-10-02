import pandas as pd
import sqlite3
from fetch_API_data import fetch_policy_data

#데이터베이스 경로 지정
db_path = "C:/Users/kdh20/Desktop/Public_data/Project/db/Database.sqlite"

# CSV 파일 경로 지정
csv_file_path = "C:/Users/kdh20/Desktop/Public_data/Project/data/여성가족부_정책자료.csv"

#테이블 이름 지정
table_name = "여성가족부_정책자료"

# 함수 호출하여 policy_data 가져오기
policy_data = fetch_policy_data(csv_file_path)


def dataframe_to_sqlite(df, db_name, table_name):
    # SQLite 데이터베이스에 연결합니다.
    conn = sqlite3.connect(db_name)
    
    
    # 데이터프레임을 SQLite 테이블로 저장합니다.
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    
    # 연결을 닫습니다.
    conn.close()

dataframe_to_sqlite(policy_data,db_path,table_name)