from abc import ABC, abstractmethod 
"""
abstract base class work
"""


class Piece(ABC):

#abstract method
    def straight(self):
        pass

class X(Piece):
    def straight(self):  # overriding abstract method
        print("This is an x shape piece")

class O(Piece):
    def straight(self):  # overriding abstract method
        print("This is a cylindrical shape piece")
        pass


class TicTacToeBoard(object):
    def squares(self):
        pass




