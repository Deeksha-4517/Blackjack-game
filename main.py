import random
from art import logo

print(logo)


def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    user_card = [random.choice(cards), random.choice(cards)]
    comp_card = [random.choice(cards), random.choice(cards)]
    user_value = sum(user_card)
    comp_value = sum(comp_card)
    print(f'Your cards drawn: {user_card}.')
    print(f'The total is {user_value}')
    print(f'the first card drawn by the computer is {comp_card[0]}')
    anon_draw = input("Type 'y' to draw another card or 'n' to skip to the end: ")

    while anon_draw == "y":
        next_card = random.choice(cards)
        if next_card == cards[0]:
            if comp_value > 21 or user_value > 21:
                cards[0] = 1
        user_card.append(next_card)
        user_value = sum(user_card)
        print(f'\nYour cards drawn: {user_card}.')
        print(f'The total is {user_value}')
        print(f'the first card drawn by the computer is {comp_card[0]}')
        anon_draw = input("Type 'y' to draw another card or 'n' to skip to the end: ")
    if anon_draw == 'n':
        print(f'Your cards drawn: {user_card}.')
        print(f'The total is {user_value}')
        print(f"Computer's cards drawn: {comp_card}.")
        print(f'The computer total is {comp_value}\n')

    if user_value > 21:
        if comp_value > 21:
            if comp_value > user_value:
                print('You win')
            elif user_value == comp_value:
                print("It's a draw")
            else:
                print('You lose')
        else:
            print('You lose')
    else:
        if user_value > comp_value:
            print('You win')
        elif user_value == comp_value:
            print("It's a draw")
        else:
            print('You lose')


blackjack()
re_gain = input("Would you like to play another game of Blackjack with me? 'Yes' or 'No'?: ").lower()
while re_gain == 'yes':
    blackjack()
    re_gain = input("Would you like to play another game of Blackjack with me? 'Yes' or 'No'?")
