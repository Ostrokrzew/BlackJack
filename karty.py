
#Moduł własny z klasami do gry w blackjacka

#klasa kart
class Card(object):
    """ Karta do gry. """
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit, face_up = True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up
    #sprawdzenie strony karty (odkryta/ zakryta)
    def __str__(self):
        if self.is_face_up:
            rep = self.rank + self.suit
        else:
            rep = "XX"
        return rep
    #obrót karty
    def flip(self):
        self.is_face_up = not self.is_face_up

#klasa ręki gracza
class Hand(object):
    """ Ręka - wszystkie karty trzymane przez gracza. """
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
           rep = ""
           for card in self.cards:
               rep += str(card) + "\t"
        else:
            rep = "<pusta>"
        return rep
    #czyszczenie ręki
    def clear(self):
        self.cards = []
    #dodanie karty
    def add(self, card):
        self.cards.append(card)
    #oddanie karty
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

#klasa talii kart
class Deck(Hand):
    """ Talia kart. """
    #uzupełnianie
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS: 
                self.add(Card(rank, suit))
    #tasowanie
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    #rozdanie
    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Nie mogę dalej rozdawać. Zabrakło kart!")



#zabezpieczenie przed bezpośrednim wywołaniem
if __name__ == "__main__":
    print("Uruchomiłeś ten moduł bezpośrednio (zamiast go zaimportować).")
    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
