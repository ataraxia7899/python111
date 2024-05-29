import os

def create_files_if_not_exist():
    # bat.txt 파일 확인 및 생성  (배팅 금액 저장 txt)
    if not os.path.isfile('bet.txt'):
        with open('bet.txt', 'w') as file:
            file.write('100000')

    # bj_score.txt 파일 확인 및 생성 (블랙잭 전적)
    if not os.path.isfile('bj_score.txt'):
        with open('bj_score.txt', 'w') as file:
            file.write('승:0,패:0,무:0\n')

    # ba_score.txt 파일 확인 및 생성 (바카라 전적)
    if not os.path.isfile('ba_score.txt'):
        with open('ba_score.txt', 'w') as file:
            file.write('승:0,패:0,무:0\n')

    # rul_score.txt 파일 확인 및 생성 (룰렛 전적)
    if not os.path.isfile('rul_score.txt'):
        with open('rul_score.txt', 'w') as file:
            file.write('승:0,패:0,무:0\n')

# 파일 생성 확인 및 생성
create_files_if_not_exist()
