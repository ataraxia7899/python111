import random

def spin_roulette():
    numbers = list(range(0, 37))  # 0부터 36까지의 숫자
    winning_number = random.choice(numbers)
    return winning_number

def determine_win(bet_type, bet_amount, winning_number):
    if bet_type == 'number':
        if bet_amount == winning_number:
            return True
    elif bet_type == 'even':
        if winning_number != 0 and winning_number % 2 == 0:
            return True
    elif bet_type == 'odd':
        if winning_number % 2 != 0:
            return True
    return False

def update_score(result, bet_amount):
    with open('rul_score.txt', 'r') as file:
        lines = file.readline().strip().split(',')

    win_count = int(lines[0].split(':')[1])
    lose_count = int(lines[1].split(':')[1])
    tie_count = int(lines[2].split(':')[1])

    if result == 'win':
        win_count += 1
    elif result == 'lose':
        lose_count += 1
    elif result == 'tie':
        tie_count += 1

    with open('rul_score.txt', 'w') as file:
        file.write(f"승:{win_count},패:{lose_count},무:{tie_count}\n")

def play_roulette():
    bet_type = input("배팅 종류를 선택하세요 (number, even, odd): ")
    bet_amount = int(input("배팅 금액을 입력하세요: "))

    winning_number = spin_roulette()
    print("베팅 종류:", bet_type)
    print("배팅 금액:", bet_amount)
    print("당첨 번호:", winning_number)

    if determine_win(bet_type, bet_amount, winning_number):
        print("축하합니다! 당첨되셨습니다!")
        update_score('win', bet_amount)
        bet_amount *= 3
        print("배팅 금액이 3배로 불려졌습니다.")
    else:
        print("아쉽지만, 당첨되지 않았습니다.")
        update_score('lose', bet_amount)
        bet_amount = 0
        print("배팅 금액을 모두 잃었습니다.")

    print("현재 전적:")
    with open('rul_score.txt', 'r') as file:
        score = file.readline()
    print(score)

# 게임 반복 실행
print("카지노 룰렛 게임에 오신 것을 환영합니다!")
print("number (숫자): \n특정한 숫자에 배팅하는 베팅 종류입니다. \n예를 들어, 플레이어가 숫자 10에 배팅한다면, \n룰렛이 돌아가서 공이 숫자 10에 떨어지면 당첨됩니다.")
print("even (짝수): \n짝수 숫자에 배팅하는 베팅 종류입니다. \n예를 들어, 플레이어가 'even'에 배팅한다면, \n룰렛이 돌아가서 공이 짝수 숫자에 떨어지면 당첨됩니다. 짝수 숫자에는 0도 포함")
print("odd (홀수): \n홀수 숫자에 배팅하는 베팅 종류입니다. \n예를 들어, 플레이어가 'odd'에 배팅한다면, \n룰렛이 돌아가서 공이 홀수 숫자에 떨어지면 당첨됩니다.")

while True:
    play_roulette()
    again = input("게임을 다시 시작하시겠습니까? (Y/N): ")
    if again.lower() != 'y':
        break
    print()
    print("카지노 룰렛 게임에 오신 것을 환영합니다!")

print("게임 종료")
 # 카지노.py 에서 파일 실행시 cmd 창이 결과값 입력되고 바로 꺼지지않게
