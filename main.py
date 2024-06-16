import random



class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Spades", "Clubs"]
    RANKS = [
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        "J",
        "Q",
        "K",
        "A",
    ]

    def __init__(self):
        self.cards = []
        self.create_deck()


    def create_deck(self):
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.cards.append((rank, suit))


    def shuffle_deck(self):
        random.shuffle(self.cards)


    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None
        

def play(deck):
    deck.shuffle_deck()
    dealers_cards = []
    players_cards = []


    for i in range(2):
        dealers_cards.append(deck.deal_card())
        players_cards.append(deck.deal_card())


    while True:
        dealer_score = count_cards(dealers_cards)
        player_score = count_cards(players_cards)
        print(f"Dealers cards: {dealers_cards} = {dealer_score}\nPlayers cards: {players_cards} = {player_score}")
        cmd = input("Hit or stand? ")
        match cmd:
            case "hit":
                hit(deck, players_cards)
                if player_score > 21:
                    print("Player Busts!")
            case "stand":
                if dealer_score < 17:
                    dealers_cards.append(deck.deal_card())
                    dealer_score = count_cards(dealers_cards)
                    if dealer_score > 21:
                        print("Dealer Busts!")
                    elif who_won(dealer_score, player_score):
                        break    
            case "quit":
                break
            case _:
                print("Invalid command!")
        

def hit(deck, cards):
    cards.append(deck.deal_card())


def who_won(dealer_score, player_score):
    if dealer_score <= 21 and dealer_score > player_score:
        print("Dealer Won!")
    elif player_score <= 21 and player_score > dealer_score:
        print("Player Won!")
    elif dealer_score > 21 and player_score <= 21:
        print("Player Won!")
    elif player_score > 21 and dealer_score <= 21:
        print("Dealer won!")


def count_cards(cards):
    card_total = 0
    for card in cards:
        if card[0] in ["j", "Q", "K"]:
            card_total += 10
        elif card[0] == "A":
            if (card_total + 11) > 21:
                card_total += 1
            else:
                card_total += 11
        else:
            card_total += card[0]
    return card_total


if __name__ == "__main__":
    cards = DeckOfCards()
    play(cards)







