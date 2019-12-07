#!/usr/bin/python

import unittest
from chess import chessPieceMoves

class TestChessMove(unittest.TestCase):

  def test_bishop(self):  
      self.assertEqual(chessPieceMoves("bishop","d5"), 'a2, a8, b3, b7, c4, c6, e4, e6, f3, f7, g2, g8, h1')
      self.assertEqual(chessPieceMoves("bishop","a1"), 'b2, c3, d4, e5, f6, g7, h8')

  def test_rook(self):  
      self.assertEqual(chessPieceMoves("rook","e6"), 'a6, b6, c6, d6, e1, e2, e3, e4, e5, e7, e8, f6, g6, h6')
      self.assertEqual(chessPieceMoves("rook","b2"), 'a2, b1, b3, b4, b5, b6, b7, b8, c2, d2, e2, f2, g2, h2')

  def test_queen(self):  
      self.assertEqual(chessPieceMoves("queen","d1"), 'a1, a4, b1, b3, c1, c2, d2, d3, d4, d5, d6, d7, d8, e1, e2, f1, f3, g1, g4, h1, h5')
      self.assertEqual(chessPieceMoves("queen","e2"), 'a2, a6, b2, b5, c2, c4, d1, d2, d3, e1, e3, e4, e5, e6, e7, e8, f1, f2, f3, g2, g4, h2, h5')

  def test_knight(self):  
      self.assertEqual(chessPieceMoves("knight","e5"), 'c4, c6, d3, d7, f3, f7, g4, g6')
      self.assertEqual(chessPieceMoves("knight","b6"), 'a4, a8, c4, c8, d5, d7')

if __name__ == '__main__':
    unittest.main()