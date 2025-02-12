''' this project was built using the logic from this YouTube video:
https://www.youtube.com/watch?v=eyoh-Ku9TCI '''

import random
cards=[2,3,4,5,6,7,8,9,10,10,10,10,11]*10
random.shuffle(cards)

def blackjack():
    bet = int(input("How much would you like to bet?\n $"))
    dealers_bet = random.randint(round(bet / 2), bet * 2)
    print(f"The Dealer would like to bet an amount of ${dealers_bet}")

    your_deck = []
    dealers_deck = []
    def pick_your_card():
        your_card=random.choice(cards)
        your_deck.append(your_card)
        print(f"You received a {your_card}")
        print(f"Your deck is now {your_deck}")
    def pick_dealers_card():
        dealers_card = random.choice(cards)
        dealers_deck.append(dealers_card)
        if len(dealers_deck)<=2:
            print(f"Dealer's deck is [{dealers_deck[0]}]")
    def sum_checker():
        condition=True
        if sum(your_deck)==21 and sum(dealers_deck)==21:
            print(f"Uh Huh! It looks like both yours and the dealer's hand have 21!\nThis game has resulted in a push!\n Your Original Amount of ${bet} is returned to you! ")
        elif sum(your_deck)>21 and sum(dealers_deck)>21:
            print(f"Uh Huh! It looks like both yours as well as the dealers' hands have been busted!\nThis game has resulted in a push!\n Your Original Amount of ${bet} is returned to you!")
        elif sum(your_deck)==21:
            print("You've won the game!\n")
            print(f"You've won ${bet*1.5}\nYour total cash is ${bet*2.5}")
            print("")
        elif sum(dealers_deck)==21:
            print(f"The Dealer has won the game!\nThe Dealer has received all your money!\nHe now has ${dealers_bet+bet} ")
        elif sum(your_deck)>21:
            print(f"Uh Huh! You've been busted!\nThe Dealer has received all your money!\nHe now has ${dealers_bet+bet}")
        elif sum(dealers_deck)>21:
            print(f"Uh Huh! The Dealer has been busted!\nYou've won twice your bet!\nYour total will be ${bet*2}")
        else:
            condition=False
        if condition:
            new_game()


    def final_checker():
        sum_checker()
        if sum(your_deck)>sum(dealers_deck):
            print(f"Your Hand is Greater than the Dealer's\nYou have won twice your bet!\nYour total amount is ${bet*2}")
        else:
            print(f"Your Hand has come up short!\nThe Dealer has taken all your money!\nHis total is now ${dealers_bet+bet}")
        new_game()

    pick_your_card()
    pick_dealers_card()
    pick_your_card()
    sum_checker()
    const=True
    while const:
        if 11 in your_deck:
            ace=int(input("You have an Ace in your deck which is currently an 11\nwould you like to convert it into a 1?\nPress 11 to keep it as 11\nPress 1 to convert it into 1\n"))
            if ace==1:
                your_deck.remove(11)
                your_deck.append(1)
                print(f"Your Deck is now {your_deck}")
            else:
                print(print(f"Your Deck remains {your_deck}"))
        elif 1 in your_deck:
            ace=int(input("You have an Ace in your deck which is currently a 1\nwould you like to convert it into a 11?\nPress 1 to keep it as 1\nPress 11 to convert it into 11\n"))
            if ace==11:
                your_deck.remove(1)
                your_deck.append(11)
                print(f"Your Deck is now {your_deck}")
            else:
                print(f"Your Deck remains {your_deck}")
        sum_checker()
        take_another_card=input("Would you like another card?\nType H for a Hit\nType M for a Miss\n")
        if take_another_card=="H":
            pick_your_card()
        if take_another_card=="M":
            const=False
    pick_dealers_card()
    print(f"dealer's deck is revealed as {dealers_deck}")

    while sum(dealers_deck)<17:
        print("The Dealer's deck is too short!\nHe picks Another card!\n")
        pick_dealers_card()
        print(f"His deck is now {dealers_deck}")
    final_checker()

def new_game():
    play = input("Would you like another round of Blackjack?\nPress Y for Yes\nPress N for No\n ")
    if play == "Y":
        print("\n" * 200)
        blackjack()
    else:
        exit()



blackjack()
