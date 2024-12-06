from DeckOfCards import DeckOfCards

# initialize card deck (print the starting deck then shuffle and print again)
def initialize_deck(deck=DeckOfCards()):
    print("Beginning deck:")
    deck.print_deck()
    print("Shuffling deck...\n")
    deck.shuffle_deck()
    print("Shuffled deck:")
    deck.print_deck()
    return deck

# game
def game(deck):
    # initialize counter vars
    user_score = 0
    card_number = 0
    dealer_score = 0
    aces = 0
    
    # first deal the user 2 cards
    for i in range(2):
        card_number += 1
        card = deck.get_card()
        # keep track of the aces if the user wants them to be worth 1
        aces = aces+1 if card.val == 11 else aces
        print(f"Your card {card_number} is: {card}")
        # add the card to the score for the user
        user_score += card.val
    # if the users score is greater than 21 and they have an ace, make the ace worth 1
    if user_score > 21 and aces > 0:
        user_score -= 10
        aces -= 1
    print("Your score:", user_score)
    # if the user wants to hit, begin while loop
    hit = input("Would you like to hit? (y/n) ")
    while hit == 'y':
        card_number += 1
        card = deck.get_card()
        aces = aces+1 if card.val == 11 else aces
        print(f"Your card {card_number} is: {card}")
        user_score += card.val
        # if the users score is greater than 21 and they have an ace, make the ace worth 1
        if user_score > 21 and aces > 0:
                user_score -= 10
                aces -= 1
        print("Your score:", user_score)
        # if the user's score is under 21 they can hit again, otherwise they are done
        if user_score < 21:   
            hit = input("Would you like to hit? (y/n) ")
        else:
            break
        
    # now for the dealer
    # reset cardnumber and amount of aces
    card_number = 0
    aces = 0
    # if the user already busts then the dealer doesn't need to show his hand
    if user_score < 22:
        # first deal two cards
        for i in range(2):
            card_number += 1
            card = deck.get_card()
            aces = aces+1 if card.val == 11 else aces
            print(f"Dealer card {card_number} is: {card}")
            dealer_score += card.val
        # if the dealer's score is under 17, the dealer hits
        while dealer_score < 17:
            card_number += 1
            card = deck.get_card()
            aces = aces+1 if card.val == 11 else aces
            print(f"Dealer hits, card {card_number} is: {card}")
            dealer_score += card.val
            # use the ace as a 1 when the dealer will bust
            if aces > 0 and dealer_score > 21: 
                dealer_score = dealer_score-10
                aces = aces-1 
        print("Dealer score:", dealer_score)
    
    # logic on who wins
    # fist if checks if the user busts
    if user_score < 22:
        # then if the dealer busts
        if dealer_score > 21:
            print("The dealer busts! You win!")
        # then if the user score beat the dealers
        elif user_score > dealer_score:
            print("Your score is higher than the dealer's! You win!")
        # then if the scores are the same
        elif user_score == dealer_score:
            print(f"You and the dealer both scored {user_score}! Dealer wins!")
        # if nothing else, then the dealers hand must have been higher
        else:
            print("Dealer's score is higher! Dealer wins!")
    else:
        print("Bust! Dealer wins!")
    

# first create the deck object
deck = DeckOfCards()
print("Welcome to BlackJack!\n")
# set up a while loop for the main game play
playing = 'y'
while playing == 'y':
    # pass deck to the function that prints and shuffles
    deck = initialize_deck(deck)
    game(deck)
    playing = input("Would you like to play again? (y/n) ")