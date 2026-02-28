import os, random, time
from datetime import datetime, timedelta
random.seed(time.time())
path = r'C:\Users\서원렬\Videos\수원성교회\교회 어린이 찬양'
files_mp4 = os.listdir(path)

# 1. 파일 목록의 복사본을 만들고 셔플(무작위 섞기)
pool = files_mp4.copy()
random.shuffle(pool)

print(f'총 파일 개수는 {len(files_mp4)}개입니다.')

start_input = input("시작일이 되는 날짜를 yy-mm-dd의 형태로 입력하세요. ex) 25-02-27: ")

try:
    current_date = datetime.strptime(start_input, "%y-%m-%d")
    plans = []
    
    for i in range(52):
        # 2. 풀(pool)에 남은 파일이 3개 미만이면 다시 전체 목록을 섞어서 보충
        if len(pool) < 3:
            new_pool = files_mp4.copy()
            random.shuffle(new_pool)
            pool.extend(new_pool) # 기존 남은 것 뒤에 새 묶음 추가
            
        # 3. 앞에서부터 3개 추출 (pop 사용)
        picked_files = [pool.pop(0) for _ in range(3)]
        
        # 결과 저장
        plans.append(f"{current_date.strftime('%Y-%m-%d')}: {picked_files}")
        current_date += timedelta(days=7)

    # 출력부 정리
    for plan in plans:
        print(plan)

except ValueError:
    print("입력 형식이 올바르지 않습니다.")