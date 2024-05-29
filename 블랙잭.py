import random

# 카드 덱 생성
suits = ['♠', '♥', '♦', '♣']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = []
for suit in suits:
    for rank in ranks:
        deck.append(rank + suit)

# 카드 점수 계산
def calculate_score(hand):
    score = 0
    num_aces = 0
    for card in hand:
        rank = card[:-1]
        if rank == 'A':
            num_aces += 1
            score += 11
        elif rank in ['K', 'Q', 'J']:
            score += 10
        else:
            score += int(rank)
    while score > 21 and num_aces > 0:
        score -= 10
        num_aces -= 1
    return score

# 전적 기록 업데이트
def update_score(result, bet_amount):
    with open('bj_score.txt', 'r') as file:
        lines = file.readlines()

    scores = lines[0].strip().split(',')
    win_count = int(scores[0].split(':')[1])
    lose_count = int(scores[1].split(':')[1])
    tie_count = int(scores[2].split(':')[1])

    if result == 'win':
        win_count += 1
    elif result == 'lose':
        lose_count += 1
    elif result == 'tie':
        tie_count += 1

    scores = [f"승:{win_count}", f"패:{lose_count}", f"무:{tie_count}"]
    updated_scores = ','.join(scores)

    with open('bj_score.txt', 'w') as file:
        file.write(updated_scores + '\n')

    # 기존 금액 확인
    with open('bet.txt', 'r') as file:
        current_money = int(file.readline().strip())

    # 승패에 따라 금액 업데이트
    if result == 'win':
        current_money += bet_amount
    elif result == 'lose':
        current_money = current_money - bet_amount if current_money >= bet_amount else 0

    # bet.txt 파일 업데이트
    with open('bet.txt', 'w') as file:
        file.write(str(current_money) + '\n')

# 게임 실행
def play_game(bet_amount):
    random.shuffle(deck)
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print('블랙잭에 오신 것을 환영합니다!')
    print('플레이어 카드:', player_hand, '점수:', calculate_score(player_hand))
    print('딜러 카드:', [dealer_hand[0], '??'], '점수: ?')

    # 플레이어 차례
    while calculate_score(player_hand) < 21:
        action = input('카드를 더 받으시겠습니까? (y/n): ')
        if action.lower() == 'y':
            player_hand.append(deck.pop())
            print('플레이어 카드:', player_hand, '점수:', calculate_score(player_hand))
        elif action.lower() == 'n':
            break
        else:
            print("잘못된 수를 입력하셨습니다.")

    player_score = calculate_score(player_hand)

    if player_score > 21:
        print('플레이어가 21점을 초과하여 패배하였습니다!')
        update_score('lose', bet_amount)  # 전적 기록 업데이트
        return

    # 딜러 차례
    print('딜러 카드:', dealer_hand, '점수:', calculate_score(dealer_hand))

    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        print('딜러가 카드를 뽑았습니다:', dealer_hand[-1])

    # 결과 출력
    print('딜러 최종 카드:', dealer_hand, '점수:', calculate_score(dealer_hand))

    dealer_score = calculate_score(dealer_hand)

    if dealer_score > 21:
        print('딜러가 21점을 초과하여 승리하였습니다! 배팅 금액이 2배로 불려졌습니다.')
        update_score('win', bet_amount)  # 전적 기록 업데이트
    elif player_score == dealer_score:
        print('무승부입니다! 배팅 금액의 변화가 없습니다.')
        update_score('tie', bet_amount)  # 전적 기록 업데이트
    elif player_score == 21:
        print('블랙잭! 플레이어가 승리하였습니다! 배팅 금액이 2배로 불려졌습니다.')
        update_score('win', bet_amount)  # 전적 기록 업데이트
    elif dealer_score == 21:
        print('딜러가 블랙잭으로 승리하였습니다! 배팅 금액을 모두 잃었습니다.')
        update_score('lose', bet_amount)  # 전적 기록 업데이트
    elif player_score > dealer_score:
        print('플레이어가 더 높은 점수로 승리하였습니다! 배팅 금액이 2배로 불려졌습니다.')
        update_score('win', bet_amount)  # 전적 기록 업데이트
    else:
        print('딜러가 더 높은 점수로 승리하였습니다! 배팅 금액을 모두 잃었습니다.')
        update_score('lose', bet_amount)  # 전적 기록 업데이트

# 게임 실행
while True:
    bet_amount_input = input('얼마를 거시겠습니까? ')
    if not bet_amount_input.isdigit():
        print("잘못된 값을 입력하셨습니다. 숫자만 입력해주세요.")
        continue

    bet_amount = int(bet_amount_input)

    play_game(bet_amount)

    play_again = input("게임을 계속 하시겠습니까? (y/n): ")
    if play_again.lower() != 'y':
        break

print("게임 종료")

