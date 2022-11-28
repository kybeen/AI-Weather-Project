### 위성사진 데이터 다운로드
from urllib.error import HTTPError
import urllib.request
import datetime

# 기준 시간: 2019년 7월 25일부터 인공지능(AI) 기반 일사량 정보를 받을 수 있음
utc = datetime.datetime(2019, 12, 17, 0)
kst = datetime.datetime(2019, 12, 17, 9)

search_time = utc
record_time = kst
while True:
    # 1시간 단위: 언제까지 돌릴 것인가?
    if search_time + datetime.timedelta(0, 60 * 60) == datetime.datetime(2022, 5, 12, 0):
        break
    
    # url parameter 세팅
    utc_tm_param = search_time.strftime('%Y%m%d%H%M')
    backup_search_time = search_time - datetime.timedelta(0, 60 * 30) # 데이터 누락 시 대체 파일 시간 (30분 전)
    backup_utc_tm_param = backup_search_time.strftime('%Y%m%d%H%M')
    download_url = f'http://api.nmsc.kma.go.kr:9080/api/GK2A/LE1B/IR087/KO/image?date={utc_tm_param}&key='
    backup_download_url = f'http://api.nmsc.kma.go.kr:9080/api/GK2A/LE1B/IR087/KO/image?date={backup_utc_tm_param}&key='

    kst_tm_param = record_time.strftime('%Y%m%d%H')
    # png 형식으로 저장할 데이터 이름 세팅
    download_file_name = f'{kst_tm_param}.png'  # 2019072500.png ~ 2022051400.png

    # urlretrieve를 통하여 바로 파일 저장
    try:
        urllib.request.urlretrieve(download_url, download_file_name)
    except HTTPError:
        urllib.request.urlretrieve(backup_download_url, download_file_name)
        print(str(record_time) + ': 자료 없음')
    print('Save: ' + download_file_name)

    search_time += datetime.timedelta(0, 60 * 60)
    record_time += datetime.timedelta(0, 60 * 60)






# # -------------------[ 하나씩만 다운받기 ]-----------------------------

# from urllib.error import HTTPError
# import urllib.request
# import datetime

# # 기준 시간: 2019년 7월 25일부터 인공지능(AI) 기반 일사량 정보를 받을 수 있음
# utc = datetime.datetime(2019, 12, 17, 0)
# kst = datetime.datetime(2019, 12, 17, 9)

# search_time = utc
# record_time = kst


# # url parameter 세팅
# utc_tm_param = search_time.strftime('%Y%m%d%H%M')
# backup_search_time = search_time - datetime.timedelta(0, 60 * 30) # 데이터 누락 시 대체 파일 시간 (30분 전)
# backup_utc_tm_param = backup_search_time.strftime('%Y%m%d%H%M')
# download_url = f'http://api.nmsc.kma.go.kr:9080/api/GK2A/LE1B/IR087/KO/image?date={utc_tm_param}&key='
# backup_download_url = f'http://api.nmsc.kma.go.kr:9080/api/GK2A/LE1B/IR087/KO/image?date={backup_utc_tm_param}&key='

# kst_tm_param = record_time.strftime('%Y%m%d%H')
# # png 형식으로 저장할 데이터 이름 세팅
# download_file_name = f'{kst_tm_param}.png'  # 2019072500.png ~ 2022051400.png

# # urlretrieve를 통하여 바로 파일 저장
# try:
#     urllib.request.urlretrieve(download_url, download_file_name)
# except HTTPError:
#     urllib.request.urlretrieve(backup_download_url, download_file_name)
#     print(str(record_time) + ': 자료 없음')
# print('Save: ' + download_file_name)