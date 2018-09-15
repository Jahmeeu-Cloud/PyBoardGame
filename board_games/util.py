"""
Util module that contains some useful functions for games

@date: 7/31/2018
@author: Larry Shi
"""

# General imports
from typing import Tuple

__all__ = ["ROW_NUM", "NUM_REF", "ID_REF", "get_id_from_pos"]

# Map front-end grid IDs with corresponding (row, col)
ROW_NUM = {0: 'one', 1: 'two', 2: 'three', 3: 'four', 4: 'five', 5: 'six', 6: 'seven', 7: 'eight', 8: 'nine'}
NUM_REF = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
ID_REF = {ROW_NUM[row] + '-' + ROW_NUM[col]: (row, col) for row in ROW_NUM.keys() for col in ROW_NUM.keys()}


# Util functions
def get_id_from_pos(pos: Tuple[int, int]) -> int:
    """
    Util function that get the ID on HTML game board
    given a position on 2D-list game board

    :param pos: the position (row, col)
    :return: the ID corresponds to the given position
    """
    for key, item in ID_REF.items():
        if item == pos:
            return key
