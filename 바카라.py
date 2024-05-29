import random
import os
import re

def create_deck():
    deck = []
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)
    random.shuffle(deck)
    return deck

def draw_card(deck):
    return deck.pop()

def calculate_card_value(card):
    rank = card[:-1]
    if rank in ['K', 'Q', 'J', '10']:
        return 0
    elif rank == 'A':
        return 1
    else:
        return int(rank)

def initialize_game():
    deck = create_deck()
    player_hand = [draw_card(deck), draw_card(deck)]
    dealer_hand = [draw_card(deck), draw_card(deck)]
    return deck, player_hand, dealer_hand

def decide_hit():
    while True:
        decision = input("카드를 더 받으시겠습니까? (Y/N): ")
        if decision.lower() == 'y':
            return True
        elif decision.lower() == 'n':
            return False
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")

def get_bet_amount():
    while True:
        try:
            bet_amount = int(input("얼마를 거시겠습니까? "))
            with open('bet.txt', 'r') as file:
                bet_amount = int(file.readline())
            if bet_amount < 0:
                print("잘못된 입력입니다. 양수를 입력해주세요.")
            else:
                return bet_amount
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")
        except FileNotFoundError:
            print("bet.txt 파일을 찾을 수 없습니다. 초기 배팅 금액을 설정해주세요.")
            return 0

def calculate_score(hand):
    score = sum(calculate_card_value(card) for card in hand)
    if score <= 10 and 'A' in hand:
        score += 10
    return score

def determine_winner(player_score, dealer_score):
    if player_score > dealer_score:
        return "플레이어가 이겼습니다!"
    elif player_score < dealer_score:
        return "딜러가 이겼습니다!"
    else:
        return "무승부입니다!"

def update_score(result, bet_amount):
    with open('ba_score.txt', 'r') as file:
        lines = file.readline().strip().split(',')

    win_count = int(re.search(r'\d+', lines[0]).group())
    lose_count = int(re.search(r'\d+', lines[1]).group())
    tie_count = int(re.search(r'\d+', lines[2]).group())

    if result == '플레이어가 이겼습니다!':
        win_count += 1
    elif result == '딜러가 이겼습니다!':
        lose_count += 1
    elif result == '무승부입니다!':
        tie_count += 1

    with open('ba_score.txt', 'w') as file:
        file.write(f"승:{win_count},패:{lose_count},무:{tie_count}\n")

def play_game():
    while True:
        bet_amount = get_bet_amount()
        deck, player_hand, dealer_hand = initialize_game()
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        print("플레이어 카드:", player_hand, "점수:", player_score)
        print("딜러 카드:", dealer_hand[0])

        while decide_hit():
            player_hand.append(draw_card(deck))
            player_score = calculate_score(player_hand)
            print("플레이어 카드:", player_hand, "점수:", player_score)
            if player_score >= 21:
                break

        while dealer_score < 17:
            dealer_hand.append(draw_card(deck))
            dealer_score = calculate_score(dealer_hand)

        print("딜러 카드:", dealer_hand, "점수:", dealer_score)
        result = determine_winner(player_score, dealer_score)
        print(result)

        if '플레이어가 이겼습니다' in result:
            bet_amount *= 2
            print("배팅 금액이 2배로 불려졌습니다.")
        else:
            bet_amount = 0
            print("배팅 금액을 모두 잃었습니다.")

        update_score(result, bet_amount)

        print("현재 전적:")
        with open('ba_score.txt', 'r') as file:
            score = file.readline()
        print(score)

        play_again = input("게임을 다시 하시겠습니까? (y/n): ")
        if play_again.lower() != 'y':
            break

play_game()
print("게임 종료")
 # 코드 실행 후 종료되지 않게 하기 위해 추가된 부분입니다.
