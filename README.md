# Vector
To implement a vector class

# ========================
# Part 1: Vector and Complex Numbers
# ========================
# ========================
# The Vector class
# ========================

# Write definitions for a class called Vector.
# Definition should include a constructor,  __str__, values for the x and y
# coordinates, and methods for addition and subtraction of vectors, scalar multiplication,
# length, and comparison.

class Vector(object):
    pass

# =========================
# The derived Complex class
# =========================

# Write definitions for a class called MyComplex that is derived from your
# Vector class.  Your definition should include methods for multiplying two
# complex numbers and computing the complex conjugate as well as an updated
# definition of __str__.

class MyComplex(Vector):
    pass
   


####################################################################################
# ========================
# Part 2: Tic-tac-toe
# ========================

# Write a simple game of tic-tac-toe.


# ========================
# The Piece class
# ========================

# Write an abstract Piece class definition.
# Your definition should include:

class Piece(object):
    pass

# =======================
# The X and O classes
# =======================

# Write definitions of X and O piece classes.
# Your definitions should include:

class X(Piece):
    pass

class O(Piece):
    pass

# =========================
# The TicTacToeBoard class
# =========================

# Write a TicTacToeBoard class definition.
# Your definition should include:

class TicTacToeBoard(object):
    pass
