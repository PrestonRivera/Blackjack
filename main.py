import random





class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Spades", "Clubs"]
    RANKS = [
        "A",
        "2",
        "3"
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "J",
        "Q",
        "K",
    ]

    def __init__(self, suit, value, card_value):
        self.suit = suit
        self.value = value
        self.card_value = card_value
        self.__cards = []
        self.create_deck()


    def create_deck(self):
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.__cards.append((rank, suit))


    def shuffle_deck(self):
        random.shuffle(self.__cards)


    def deal_card(self):
        if len(self.__cards) > 0:
            return self.__cards.pop()
        else:
            return None
        

def play():
    while True:
        cmd = input("Hit or pass? ")
        match cmd:
            case "hit":
                hit()
            case "stand":
                continue
                # calc_score()
            case "quit":
                break
            case _:
                print("Invalid command!")

def hit():
    





    if __name__ == "__main__":
        play()







