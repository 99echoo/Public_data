import subprocess
import os

# deliver.py를 실행하는 함수입니다.
def run_deliver_script():
    # 현재 스크립트의 디렉토리 경로를 가져옵니다.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # deliver.py의 전체 경로를 생성합니다.
    deliver_script_path = os.path.join(script_dir, 'deliver.py')
    subprocess.run(["python", deliver_script_path])

if __name__ == "__main__":
    run_deliver_script()