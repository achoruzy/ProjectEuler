# PROBLEM 54 Poker hands

# https://projecteuler.net/problem=54


# ----------- PSEUDOCODE -------------

# load the file and loop over rows
#   split each row for two players
#   check card rankings for players and compare
#   add 1 for the winner
# print player 1 wins

# -------------- CODE ----------------
from time import time


def timing(func):
    """ Decorator function for calculating working time of another function."""
    def wrapper(*args, **kwargs):
        time_1 = time()
        return_var = func(*args, **kwargs)
        time_2 = time()
        print('Function worked: ', str(time_2-time_1)[:5], ' sec.')
        return return_var
    return wrapper()


def get_file_data() -> list:
    """ Generator function yields next list of cards in txt file row"""
    file_path = './0054poker.txt'
    with open(file_path, mode='r') as file:
        while True:
            line = file.readline()
            if len(line) == 0:
                raise StopIteration
            line_list = line[0:-1].split(' ')
            yield line_list


def split_players(card_list: list) -> tuple:
    """ Returns cards split for players """
    cards_split = []
    no_cards_for_plr = int(len(card_list) / 2)
    no_of_plrs = int(len(card_list) / 5)

    for i in range(0, no_of_plrs):
        ran_start = i * no_cards_for_plr
        ran_stop = ((i + 1) * no_cards_for_plr)
        plr = [i for i in card_list[ran_start:ran_stop]]
        cards_split.append(plr)
    return cards_split


def compare_cards(plr1: int, pl2: int, *args) -> int:
    """ Compares card rankings of players. """
    rankings = [i for i in (plr1, pl2, *args)]
    winner = max(rankings)
    winner_index = rankings.index(winner)
    return winner_index+1


class Cards():
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    colors = ['H', 'C', 'S', 'D']
    scoring = {k: v for v, k in enumerate(values)}

    def __init__(self, cards: list):
        self.cards = cards
        self.cards.sort()
        self.cards_string = self._cards_str()

    def _cards_str(self):
        cards_string = ''

        for i in self.cards:
            cards_string += i

        return cards_string

    def _all_color(self) -> bool:
        """ Checks if all cards are the same color."""
        check_set = set()

        for card in self.cards:
            check_set.add(card[1])

        if len(check_set) != 5:
            return True
        return False

    def no_ranked_cards(self) -> bool:
        """ Method checks if card set has any ranked figures. If has, returns True."""
        for i in self.values:
            if self.cards_string.count(i) > 1:
                return False
        for i in self.colors:
            if self.cards_string.count(i) > 2:
                return False

        return True

    def highest_card(self) -> dict:
        """ Method checks the highest card in card set."""
        highest_card = {}
        highest_score = 0

        for card in self.cards:
            key = card[0]
            if self.scoring[key] > highest_score:
                highest_score = self.scoring[key]
                highest_card = {key: self.scoring[key]}

        return highest_card

    def repeated_card_values(self) -> dict:
        """ Method checks if pairs, threes and fours of cards of one kind occurs in a set."""
        result = dict()

        for val in self.values:
            count = self.cards_string.count(val)
            if count > 1:
                result.update({val: count})

        return result

    def straight_flush(self) -> dict:
        """ Method checks Straight, Flush, Straight Flush and Royal Flush type figures for a card set."""
        result = {}

        if self._all_color():
            highest = self.highest_card()
            val = list(highest.values())[0]
            result = {'Flush': val}

        return result

# -------------- TESTS ---------------


def test_get_file_data():
    # given
    iterator = get_file_data()
    # when
    first_row = next(iterator)
    # then
    assert first_row == ['8C', 'TS', 'KC', '9H',
                         '4S', '7D', '2S', '5D', '3S', 'AC']
    assert next(iterator) == ['5C', 'AD', '5D', 'AC',
                              '9C', '7C', '5H', '8D', 'TD', 'KS']


def test_split_players():
    # given
    card_list = ['8C', 'TS', 'KC', '9H',
                 '4S', '7D', '2S', '5D', '3S', 'AC']
    # when
    result = split_players(card_list)
    # then
    assert result == [['8C', 'TS', 'KC', '9H',
                       '4S'], ['7D', '2S', '5D', '3S', 'AC']]


def test_Cards():
    card_set_1 = ['8C', 'TS', 'KC', '9H', '4S']
    card_set_2 = ['8C', '8S', 'TS', 'JS', 'QS']
    card_set_3 = ['8C', '8S', 'TS', 'TC', 'TD']
    card_set_4 = ['QC', 'QS', 'QD', 'QH', 'AS']
    card_set_5 = ['2S', '5S', '7S', 'TS', 'QS']
    card_set_6 = ['8C', '8S', 'TS', 'TC', 'TD']
    card_set_7 = ['QC', 'QS', 'QD', 'QH', 'AS']

    cards_1 = Cards(card_set_1)
    cards_2 = Cards(card_set_2)
    cards_3 = Cards(card_set_3)
    cards_4 = Cards(card_set_4)
    cards_5 = Cards(card_set_5)
    cards_6 = Cards(card_set_6)
    cards_7 = Cards(card_set_7)

    # then
    assert cards_1.no_ranked_cards() == True
    assert cards_2.no_ranked_cards() == False
    assert cards_1.highest_card() == {'K': 11}
    assert cards_1.repeated_card_values() == {}
    assert cards_2.repeated_card_values() == {'8': 2}
    assert cards_3.repeated_card_values() == {'8': 2, 'T': 3}
    assert cards_4.repeated_card_values() == {'Q': 4}
    assert cards_5.straight_flush() == {'Flush': 10}


def test_compare_cards():
    # given
    plr1 = 12
    plr2 = 44
    # when
    result = compare_cards(plr1, plr2)
    # then
    assert result == 2
    assert compare_cards(11, 32, 44, 21, 87) == 5


# --------------- RUN ---------------
if __name__ == '__main__':
    pass

# ------------ RESULT -------------
