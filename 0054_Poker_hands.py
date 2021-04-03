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
    def compare_cards(scores: list, highest_cards: list) -> int:
        """ Compares card rankings of players. """

        # Known issue: Cards comparission works only for highest cards in sets, so if in both sets are same cards

        score_values = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'T': 10,
            'J': 11,
            'Q': 12,
            'K': 13,
            'A': 14,
            'Pair': 20,
            'Two Pairs': 30,
            'Triple': 40,
            'Straight': 50,
            'Flush': 60,
            'Full House': 70,
            'Four of a Kind': 80,
            'Straight Flush': 90,
        }

        score_list = []
        score_highest = []

        # Scores are equal -> compare highest cards
        if scores[0] == scores[1]:
            for player in highest_cards:
                key = list(player.keys())[0]
                value = score_values.get(key)
                score_highest.append(value)

            if score_highest[0] == score_highest[1]:
                raise Exception('Tie in first highest card check!')

            winner = score_highest.index(max(score_highest))+1
            return winner

        # Scores are same type but different score highest card
        plr1_key = list(scores[0].keys())[0]
        plr2_key = list(scores[1].keys())[0]
        if plr1_key == plr2_key:
            if scores[0].get(plr1_key) > scores[1].get(plr2_key):
                winner = 1
            else:
                winner = 2
            return winner

            # Else
        for player in scores:
            score = list(player.keys())[0]
            value = score_values.get(score)
            score_list.append(value)

        check_set = set(score_list)

        winner = score_list.index(max(score_list))+1
        return winner


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
            if check > 4:
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
        """ Method checks if pairs, threes and fours of cards of one kind occurs in a set. If no repeated cards found then returns highest card"""
        help_result = dict()
        result = dict()

        for val in self.values:
            count = self.cards_string.count(val)
            if count > 1:
                help_result.update({val: count})

        if len(help_result) == 0:
            return self.highest_card()

        dict_key = list(help_result.keys())
        dict_val = list(help_result.values())
        val_set = set(dict_val)
        key = dict_key[0]
        value = help_result.get(key)
        score = self.scoring.get(key)

        if len(help_result) > 1:
            key_for_3 = ''
            score_for_2 = 0

            if val_set == {2}:
                for key in dict_key:
                    val = help_result.get(key)
                    if val == 2:
                        scr = self.scoring.get(key)
                        if scr > score_for_2:
                            score_for_2 = scr

                result.update({'Two Pairs': score_for_2})
                return result

            elif val_set == {2, 3}:
                for key in dict_key:
                    if help_result.get(key) == 3:
                        key_for_3 = key

                score_tri = self.scoring.get(key_for_3)
                result.update({'Full House': score_tri})
                return result

        if value == 2:
            result.update({'Pair': score})
            return result
        elif value == 3:
            result.update({'Triple': score})
            return result
        elif value == 4:
            result.update({'Four of a Kind': score})
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
    compare = [{'Full House': 10}, {'K': 13}]
    highest = [{'Q': 12}, {'K': 13}]
    # when
    result = operator.compare_cards(compare, highest)
    # then
    assert result == 1
    assert operator.compare_cards(
        [{'Full House': 10}, {'Full House': 10}], [{'Q': 12}, {'K': 13}]) == 2


def test_Cards():
    card_set_1 = ['8C', 'TS', 'KC', '9H', '4S']
    card_set_2 = ['8C', '8S', 'TS', 'JS', 'QS']
    card_set_3 = ['8C', '8S', 'TS', 'TC', 'TD']
    card_set_4 = ['QC', 'QS', 'QD', 'QH', 'AS']
    card_set_5 = ['2S', '5S', '7S', 'TS', 'QS']
    card_set_6 = ['4S', '5S', '6S', '7S', '8S']
    card_set_7 = ['QC', 'QS', 'QD', 'QH', 'AS']
    card_set_8 = ['QC', 'QS', 'QD', 'KH', 'AS']
    card_set_9 = ['3S', 'QH', '5S', '6S', 'AS']
    card_set_10 = ['6D', '6C', 'TD', 'TH', 'KD']

    cards_1 = Cards(card_set_1)
    cards_2 = Cards(card_set_2)
    cards_3 = Cards(card_set_3)
    cards_4 = Cards(card_set_4)
    cards_5 = Cards(card_set_5)
    cards_6 = Cards(card_set_6)
    cards_7 = Cards(card_set_7)
    cards_8 = Cards(card_set_8)
    cards_9 = Cards(card_set_9)
    cards_10 = Cards(card_set_10)

    # then
    assert cards_1.has_ranked_cards() == False
    assert cards_2.has_ranked_cards() == True
    assert cards_9.has_ranked_cards() == False
    assert cards_1.highest_card() == {'K': 13}
    assert cards_1.repeated_card_values() == {'K': 13}
    assert cards_2.repeated_card_values() == {'Pair': 8}
    assert cards_3.repeated_card_values() == {'Full House': 10}
    assert cards_4.repeated_card_values() == {'Four of a Kind': 12}
    assert cards_8.repeated_card_values() == {'Triple': 12}
    assert cards_5.straight_flush() == {'Flush': 12}
    assert cards_6.straight_flush() == {'Straight Flush': 8}
    assert cards_6.score() == {'Straight Flush': 8}
    assert cards_3.score() == {'Full House': 10}
    assert cards_9.score() == {'A': 14}
    assert cards_10.score() == {'Two Pairs': 10}


# --------------- RUN ---------------
if __name__ == '__main__':
    path = './0054poker.txt'
    file = FileHandler(path)

    plr1_wins = 0
    plr2_wins = 0

    for i in file.get_file_data():
        print(i)
        player_1 = Cards(i[0])
        player_2 = Cards(i[1])

        scores = [player_1.score(), player_2.score()]
        highest_cards = [player_1.highest_card(), player_2.highest_card()]

        winner = PokerOperator.compare_cards(scores, highest_cards)

        print(f'Player 1 score: {scores[0]}.',
              f'Player 2 score: {scores[1]}.', f'\nWinner is player {winner}')

        if winner == 1:
            plr1_wins += 1
        elif winner == 2:
            plr2_wins += 1
        else:
            raise Exception('Something is wrong!')

    print('Player 1 wins:', plr1_wins, '\nPlayer 2 wins:', plr2_wins)

# ------------ RESULT -------------

# Player 1 wins: 376
# Player 2 wins: 624
