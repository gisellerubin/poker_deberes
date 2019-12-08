import random
suits = ["♠", "♥", "♦", "♣"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def __lt__(self, other):
        return ranks.index(self.get_rank()) < ranks.index(other.get_rank())

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)

    def __sub__(self, other):
        return ranks.index(self.get_rank()) - ranks.index(other.get_rank())

    # def __ne__(self, other):
    #    return ranks.index(self.get_rank()) != ranks.index(other.get_rank())


class Deck(object):
    def __init__(self):
        self.cards = []
        for s in suits:
            for r in ranks:
                self.cards.append(Card(s, r))

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        deck = ""
        for i in range(0, 52):
            deck += str(self.cards[i]) + " "
        return deck

    def take_one(self):
        return self.cards.pop(0)


class Hand(object):
    def __init__(self, deck):
        self.cards = []
        for i in range(5):
            self.cards.append(deck.take_one())

    def __str__(self):
        hand = ""
        for i in range(5):
            hand += str(self.cards[i]) + " "
        return hand

    def is_pair(self):
        self.cards.sort()
        for i in range(5):
            for j in range(i+1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    return True
        return False

    def is_two_pair(self):
        self.cards.sort()
        if self.cards[0].get_rank() == self.cards[1].get_rank() and \
            self.cards[2].get_rank() == self.cards[3].get_rank():
            return True
        elif self.cards[1].get_rank() == self.cards[2].get_rank() and \
            self.cards[3].get_rank() == self.cards[4].get_rank():
            return True
        elif self.cards[0].get_rank() == self.cards[1].get_rank() and \
            self.cards[3].get_rank() == self.cards[4].get_rank():
            return True
        return False

    def is_three_of_a_kind(self):
        self.cards.sort()
        for i in range(5):
            for j in range(i+1, 5):
                for k in range(j+1, 5):
                    if self.cards[i].get_rank() == self.cards[j].get_rank() == self.cards[k].get_rank():
                        return True
        return False

    def is_straight(self):
        # We need to sort the hand
        self.cards.sort()
        # special case A 2 3 4 5 ( 2 3 4 5 A )
        if self.cards[0].get_rank() == "2" and \
            self.cards[1].get_rank() == "3" and \
            self.cards[2].get_rank() == "4" and \
            self.cards[3].get_rank() == "5" and \
            self.cards[4].get_rank() == "A":
            return True

        for i in range(4):
            rank1 = self.cards[i].get_rank()
            rank2 = self.cards[i+1].get_rank()
            value1 = ranks.index(rank1)
            value2 = ranks.index(rank2)
            if value1 + 1 != value2:
                return False
        return True

    def is_flush(self):
        self.cards.sort()
        palo = self.cards[0].get_suit()
        for i in range(1, 5):
            if self.cards[i].get_suit() != palo:
                return False
        return True

    def is_full_house(self):
        self.cards.sort()
        if self.cards[0].get_rank() == self.cards[1].get_rank() and \
            self.cards[2].get_rank() == self.cards[4].get_rank():
            return True
        elif self.cards[0].get_rank() == self.cards[2].get_rank() and \
            self.cards[3].get_rank() == self.cards[4].get_rank():
            return True
        return False

    def is_four_of_a_kind(self):
        self.cards.sort()
        if self.cards[0].get_rank() == self.cards[3].get_rank():
            return True
        elif self.cards[1].get_rank() == self.cards[4].get_rank():
            return True
        return False

    def is_straight_flush(self):
        palo = self.cards[0].get_suit()
        # We need to sort the hand
        self.cards.sort()
        # special case A 2 3 4 5 ( 2 3 4 5 A )
        for i in range(1, 5):
            if self.cards[i].get_suit() != palo:
                return False

        if self.cards[0].get_rank() == "2" and \
                self.cards[1].get_rank() == "3" and \
                self.cards[2].get_rank() == "4" and \
                self.cards[3].get_rank() == "5" and \
                self.cards[4].get_rank() == "A":
            return True

        for i in range(4):
            rank1 = self.cards[i].get_rank()
            rank2 = self.cards[i + 1].get_rank()
            value1 = ranks.index(rank1)
            value2 = ranks.index(rank2)
            if value1 + 1 != value2:
                return False

        return True

    def is_royal_flush(self):
        self.cards.sort()
        palo = self.cards[0].get_suit()
        for i in range(1, 5):
            if self.cards[i].get_suit() != palo:
                return False
        if self.cards[0].get_rank() == "10" and \
            self.cards[1].get_rank() == "J" and \
            self.cards[2].get_rank() == "Q" and \
            self.cards[3].get_rank() == "K" and \
            self.cards[4].get_rank() == "A":
            return True
        return False


counter_pair = 0
counter_twoPair = 0
counter_three = 0
counter_straight = 0
counter_flush = 0
counter_fullHouse = 0
counter_four = 0
counter_straightFlush = 0
counter_royalFlush = 0
n = 100000
print("WE DEALT", n, "HANDS WITH", n, "different new decks that have been shuffled.")
print("THESE ARE THE DATA THAT WE GOT IN THE EXPERIMENT.")
print("")
for i in range(n):
    new_deck = Deck()
    new_deck.shuffle()
    hand = Hand(new_deck)
    if hand.is_pair():
        counter_pair += 1
    if hand.is_two_pair():
        counter_twoPair += 1
    if hand.is_three_of_a_kind():
        counter_three += 1
    if hand.is_straight():
        counter_straight += 1
    if hand.is_flush():
        counter_flush += 1
    if hand.is_full_house():
        counter_fullHouse += 1
    if hand.is_four_of_a_kind():
        counter_four += 1
    if hand.is_straight_flush():
        counter_straightFlush += 1
    if hand.is_royal_flush():
        counter_royalFlush += 1

print("Number of Pairs: ", counter_pair)
print("Number of Two pairs: ", counter_twoPair)
print("Number of Three of a kind: ", counter_three)
print("Number of Straights: ", counter_straight)
print("Number of Flushes: ", counter_flush)
print("Number of Full houses", counter_fullHouse)
print("Number of Four of a kind: ", counter_four)
print("Number of Straight flushes: ", counter_straightFlush)
print("Number of Royal flushes: ", counter_royalFlush)

print("")
print("THESE ARE THE STATS: ")
print("Probability of a Pair: ", float(counter_pair/n))
print("Probability of a Two pair: ", float(counter_twoPair/n))
print("Probability of a Three of a kind: ", float(counter_three/n))
print("Probability of a Straight: ", float(counter_straight/n))
print("Probability of a Flush: ", float(counter_flush/n))
print("Probability of a Full house: ", float(counter_fullHouse/n))
print("Probability of a Four of a kind: ", float(counter_four/n))
print("Probability of a Straight Flush: ", float(counter_straightFlush/n))
print("Probability of a Royal Flush: ", float(counter_royalFlush/n))