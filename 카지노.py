import tkinter as tk
import os

def run_roulette():
    os.system("룰렛.py")

def run_baccarat():
    os.system("바카라.py")

def run_blackjack():
    os.system("블랙잭.py")

def run_firstset():
    os.system("python 파일생성.py")
    
def show_roulette_rules():
    os.startfile("룰렛_사진.png")

def show_baccarat_rules():
    os.startfile("바카라_사진.png")

def show_blackjack_rules():
    os.startfile("블랙잭_사진.png")

window = tk.Tk()
window.title("카지노에 온 것을 환영합니다!")

# 창 크기 설정
window.geometry("700x550")

# 환영 메시지
welcome_label = tk.Label(window, text="카지노에 온 것을 환영합니다!", font=("Helvetica", 20))
welcome_label.pack(pady=(20, 0))

# 버튼 생성
button_frame = tk.Frame(window)
button_frame.pack(pady=(0, 0))

start_button = tk.Button(button_frame, text="처음 오셨다면 클릭", font=("Helvetica", 20), command=run_firstset, bg="yellow")
start_button.pack(side="left", padx=10)

# 게임 선택 버튼 생성
game_frame = tk.Frame(window)
game_frame.pack(pady=15)

roulette_button = tk.Button(game_frame, text="룰렛", font=("Helvetica", 20), command=run_roulette, width=10, height=3, bg="#BA55D3")
roulette_button.pack(side="left", padx=10)

baccarat_button = tk.Button(game_frame, text="바카라", font=("Helvetica", 20), command=run_baccarat, width=10, height=3, bg="#BA55D3")
baccarat_button.pack(side="left", padx=10)

blackjack_button = tk.Button(game_frame, text="블랙잭", font=("Helvetica", 20), command=run_blackjack, width=10, height=3, bg="#BA55D3")
blackjack_button.pack(side="left", padx=10)

# 룰 버튼 생성
rules_frame = tk.Frame(window)
rules_frame.pack(pady=20)

roulette_rules_button = tk.Button(rules_frame, text="룰렛 룰", font=("Helvetica", 20), command=show_roulette_rules, width=8, height=2, bg="gray")
roulette_rules_button.pack(side="left", padx=10)

baccarat_rules_button = tk.Button(rules_frame, text="바카라 룰", font=("Helvetica", 20), command=show_baccarat_rules, width=8, height=2, bg="gray")
baccarat_rules_button.pack(side="left", padx=10)

blackjack_rules_button = tk.Button(rules_frame, text="블랙잭 룰", font=("Helvetica", 20), command=show_blackjack_rules, width=8, height=2, bg="gray")
blackjack_rules_button.pack(side="left", padx=10)

# 승률 텍스트
score_frame = tk.Frame(window)
score_frame.pack(pady=5)

rul_score_label = tk.Label(score_frame, text="룰렛 승률:", font=("Helvetica", 9), anchor="w")
rul_score_label.pack(side="left", padx=10)

ba_score_label = tk.Label(score_frame, text="바카라 승률:", font=("Helvetica", 9), anchor="w")
ba_score_label.pack(side="left", padx=10)

bj_score_label = tk.Label(score_frame, text="블랙잭 승률:", font=("Helvetica", 9), anchor="w")
bj_score_label.pack(side="left", padx=10)

# 돈 액수 표시
money_frame = tk.Frame(window)
money_frame.pack(pady=0)

money_label = tk.Label(money_frame, text="보유 금액:", font=("Helvetica", 25), anchor="center")
money_label.pack(side="left", padx=10)

# 승률 파일 읽어오기
try:
    with open('ba_score.txt', 'r', encoding='cp949') as file:
        ba_score = file.read()
    with open("bj_score.txt", "r", encoding="cp949") as file:
        bj_score = file.read()
    with open("rul_score.txt", "r", encoding='cp949') as file:
        rul_score = file.read()

    # 승률 표시
    ba_score_label.config(text=f"바카라 승률: {ba_score}")
    bj_score_label.config(text=f"블랙잭 승률: {bj_score}")
    rul_score_label.config(text=f"룰렛 승률: {rul_score}")
    
    # 통합된 보유 금액 가져오기
    with open("bet.txt", "r", encoding="utf-8") as file:
        total_money = file.read()
    
    # 돈 액수 표시
    money_label.config(text=f"바카라 보유 금액: ${total_money}")
    
except FileNotFoundError:
    ba_score_label.config(text="바카라 승률: 스코어 파일을 찾을 수 없습니다.")
    bj_score_label.config(text="블랙잭 승률: 스코어 파일을 찾을 수 없습니다.")
    rul_score_label.config(text="룰렛 승률: 스코어 파일을 찾을 수 없습니다.")
    
    money_label.config(text="보유 금액: bet 파일을 찾을 수 없습니다.")

window.mainloop()
