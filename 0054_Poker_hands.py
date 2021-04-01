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


class FileHandler():
    """Class for handling poker files."""

    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_file_data(self) -> list:
        """ Generator function yields next list of cards in txt file row"""
        with open(self.file_path, mode='r') as file:
            while True:
                line = file.readline()
                if len(line) == 0:
                    break
                line_list = line[0:-1].split(' ')

                split_players = self._split_players(line_list)

                yield split_players

    def _split_players(self, card_list: list) -> tuple:
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


class PokerOperator():
    """Class works as operator for players and game."""

    @staticmethod
    def compare_cards(cards: list) -> int:
        """ Compares card rankings of players. """
        player_sets = [i for i in cards]
        score_of_players = []

        for i in player_sets:
            plr_cards = Cards(i)
            score = plr_cards.score()
            score_of_players.append(score)

        return score_of_players


class Cards():
    """Class represents cards in player's hand."""
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    colors = ['H', 'C', 'S', 'D']
    scoring = {k: v for v, k in enumerate(values, start=2)}

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
            color = card[1]
            check_set.add(color)

        if len(check_set) == 1:
            return True
        return False

    def _consecutive_cards(self) -> bool:
        """ Checks if all cards are consecutive."""
        check_list = [self.scoring.get(card[0]) for card in self.cards]
        check_list.sort()

        for i in range(1, 5):
            if check_list[0] != check_list[i]-i:
                return False
        return True

    def has_ranked_cards(self) -> bool:
        """ Method checks if card set has any ranked figures. If has, returns True."""

        for i in self.values:
            check = self.cards_string.count(i)
            if check > 1:
                return True

        for i in self.colors:
            check = self.cards_string.count(i)
            if check >= 4:
                return True

        if self._consecutive_cards():
            return True

        return False

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

        # REVISE FOR RESULT IN FORM {'Pair/Triple/Four/3+2', scoring}

        return result

    def straight_flush(self) -> dict:
        """ Method checks Straight, Flush, Straight Flush and Royal Flush type figures for a card set."""
        result = {}

        consecutive_cards = self._consecutive_cards()
        all_color = self._all_color()
        highest = self.highest_card()
        val = list(highest.values())[0]

        if consecutive_cards and all_color:
            result = {'Straight Flush': val}
        elif consecutive_cards:
            result = {'Straight': val}
        elif all_color:
            result = {'Flush': val}
        else:
            return None
        return result

    def score(self) -> dict:
        """ Method returns highest score rank of the card set."""
        if not self.has_ranked_cards():
            return self.highest_card()

        check = self.straight_flush()
        if check != None:
            return check
        else:
            return self.repeated_card_values()


# -------------- TESTS ---------------


def test_FileHandler():
    # given
    test_file_path = './0054poker.txt'
    test_file_handler = FileHandler(test_file_path)

    iterator = test_file_handler.get_file_data()
    # when
    first_row = next(iterator)
    # then
    assert first_row == [['8C', 'TS', 'KC', '9H',
                          '4S'], ['7D', '2S', '5D', '3S', 'AC']]
    assert next(iterator) == [['5C', 'AD', '5D', 'AC',
                               '9C'], ['7C', '5H', '8D', 'TD', 'KS']]


def test_PokerOperator():
    # given
    operator = PokerOperator()
    compare = [['QC', 'QS', 'QD', 'QH', 'AS'], ['7D', '2S', '5D', '3S', 'AC']]
    # when
    result = operator.compare_cards(compare)
    # then
    assert result == 1


def test_Cards():
    card_set_1 = ['8C', 'TS', 'KC', '9H', '4S']
    card_set_2 = ['8C', '8S', 'TS', 'JS', 'QS']
    card_set_3 = ['8C', '8S', 'TS', 'TC', 'TD']
    card_set_4 = ['QC', 'QS', 'QD', 'QH', 'AS']
    card_set_5 = ['2S', '5S', '7S', 'TS', 'QS']
    card_set_6 = ['4S', '5S', '6S', '7S', '8S']
    card_set_7 = ['QC', 'QS', 'QD', 'QH', 'AS']

    cards_1 = Cards(card_set_1)
    cards_2 = Cards(card_set_2)
    cards_3 = Cards(card_set_3)
    cards_4 = Cards(card_set_4)
    cards_5 = Cards(card_set_5)
    cards_6 = Cards(card_set_6)
    cards_7 = Cards(card_set_7)

    # then
    assert cards_1.has_ranked_cards() == False
    assert cards_2.has_ranked_cards() == True
    assert cards_1.highest_card() == {'K': 13}
    assert cards_1.repeated_card_values() == {}
    assert cards_2.repeated_card_values() == {'8': 2}
    assert cards_3.repeated_card_values() == {'8': 2, 'T': 3}  # Full House
    assert cards_4.repeated_card_values() == {'Q': 4}
    assert cards_5.straight_flush() == {'Flush': 12}
    assert cards_6.straight_flush() == {'Straight Flush': 8}
    assert cards_6.score() == {'Straight Flush': 8}
    assert cards_3.score() == {'8': 2, 'T': 3}


# --------------- RUN ---------------
if __name__ == '__main__':
    path = './0054poker.txt'
    file = FileHandler(path)

    for i in file.get_file_data():
        print(i)

# ------------ RESULT -------------
