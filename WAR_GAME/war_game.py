import random

class Card:
    card_suits = ["hearts","dimonds","spades","clubs"]
    card_ranks = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"Jack":11,"Queen":12,"King":13,"Ace":14}
    def __init__(self, suit, rank):
        self.suit = suit.capitalize()  #harts dimonds spades clubs
        self.rank = rank.capitalize()
        self.value = self.card_ranks[rank]
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    def __int__(self):
        return  self.value
        
        
        
class Deck(Card):
    def __init__(self):
        self.deck = []
        self.createDeck()

    def createDeck(self):
        for suit in Card.card_suits:
            for rank in Card.card_ranks.items():
                card_inst = Card(suit,rank[0])
                self.deck.append(card_inst)
    def shuffleDeck(self):
        random.shuffle(self.deck)

class Player:
    def __init__(self,cards,name):
        self.name = name
        self.card_set = cards
    def give_top_card(self):
        '''
        :return: return fist top card from list
        '''
        return self.card_set.pop(0)
    def recieve_cards(self, cards):
        '''
        add cards to card set at the end
        :param cards: has to be list
        :return: void
        '''
        random.shuffle(cards)
        for card in cards:
            self.card_set.insert(len(self.card_set),card)

    # def __len__(self):
    #     '''
    #     It returns how many cards do player have
    #     :return:
    #     '''
    #     return len(self.card_set)

class Game_Running(Player,Deck):

    def __init__(self):
        self.deck_of_cards = Deck()
        self.deck_of_cards.shuffleDeck()
        self.player1 = Player([],"Bob")
        self.player2 = Player([],"Steve")

    def compare_values(self,player1_card,player2_card):
        #rekurencyjnie jeżeli są równe ponownie wystaw karty, jeżeli majatakie same karty i nie maja więcej kart remis
        if player1_card.value() == player1_card.value():
            pass
            #compare_values()
    def play_war_game(self):
        #porównać karty z wierzchu:
        #jeżeli jedna większa od drugiej, idą na koniec stosu tego który miał większą wartość
        #jeżeli są równe, odłożyć do buforu, dodać po 3 od obu userów i ponownie porównać

        #jezeli nikt nie ma kart remis
        round_counter = 0
        p1_tmp = []
        p2_tmp = []
        pool = []
        winholder = tuple((False, ""))
        is_there_a_winner = False
        while is_there_a_winner == False:
            if len(self.player1.card_set) == 0 or len(self.player2.card_set) == 0:
                pass
            winholder = self.check_winner()
            if winholder[0] == True:
                break
            p1_tmp = self.player1.give_top_card()
            p2_tmp = self.player2.give_top_card()
            pool.append(p1_tmp)
            pool.append(p2_tmp)
            if p1_tmp.value > p2_tmp.value:
                self.player1.recieve_cards(pool)
                pool.clear()
            elif p1_tmp.value < p2_tmp.value:
                self.player2.recieve_cards(pool)
                pool.clear()
            elif p1_tmp.value == p2_tmp.value:
                for i in range(1,4):
                    if len(self.player1.card_set) >  0:
                        pool.append(self.player1.give_top_card())
                    else:
                        winholder = self.check_winner()
                    if len(self.player2.card_set) > 0:
                        pool.append(self.player2.give_top_card())
                    else:
                        winholder = self.check_winner()

            if len(pool) > 2:
                continue

            winholder = self.check_winner()
            is_there_a_winner = winholder[0]
            round_counter +=1
        print(winholder[1])







    def check_winner(self):

        if len(self.player1.card_set) == 0 and len(self.player2.card_set) != 0:
            return tuple((True, "Player 2 Wins"))
        elif len(self.player2.card_set) == 0 and len(self.player1.card_set) != 0:
            return tuple((True, "Player 1 Wins"))
        elif len(self.player2.card_set) == 0 and len(self.player1.card_set) == 0:
            return tuple((True, "Draw!"))
        return tuple((False, ""))

    def deal_cards(self):
        self.player1.recieve_cards(self.deck_of_cards.deck[int(len(self.deck_of_cards.deck)/2):])
        self.player2.recieve_cards(self.deck_of_cards.deck[0:int(len(self.deck_of_cards.deck)/2)])


if __name__ == '__main__':
    the_game = Game_Running()


