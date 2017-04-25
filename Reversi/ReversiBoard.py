#!/usr/bin/python
# -*- coding: utf-8 -*-
import ReversiCommon as rc
import copy


class ReversiBoard:
    """ オセロ盤 """
    def __init__(self,board=None,turn=None):
        if board:
            #前の状態を引き継ぎ
            self.board = board
            self.turn = turn
        else:
            #ボード初期化
            self.size = rc.SIZE 
            self.board = [[rc.NONE for i in range(rc.SIZE)] for j in range(rc.SIZE)]
            self.board[rc.SIZE/2-1][rc.SIZE/2-1] = rc.WHITE
            self.board[rc.SIZE/2][rc.SIZE/2] = rc.WHITE
            self.board[rc.SIZE/2-1][rc.SIZE/2] = rc.BLACK
            self.board[rc.SIZE/2][rc.SIZE/2-1] = rc.BLACK
            # 黒のターンから開始
            self.turn = rc.BLACK

    def getPlayer(self):
        """プレイヤーを返す"""
        if self.turn == rc.BLACK:
            return 1 #BLACK
        else:
            return 2 #WHITE

    def getTrun(self):
        return self.turn

    def getPieces(self):
        """盤面を返す"""
        return self.board

    def getPieceColor(self,x,y):
        """マスの色を返す"""
        if self.board[x][y] == rc.BLACK:
            return 1
        elif self.board[x][y] == rc.WHITE:
            return 2
        else:
            return 0

    def change_turn(self):
        """ 交代 """
        if self.turn == rc.WHITE:
            self.turn = rc.BLACK
        else:
            self.turn = rc.WHITE

    def put_stone(self, color, x, y):
        """ 置く & ひっくり返す """
        self.board = rc.put_stone(self.board, color, x, y)

        # プレーヤ交代
        enemy = not(color)
        #置ける場所がない場合は置かずに交代
        if len(rc.get_puttable_points(self.board, enemy)) > 0:
            self.change_turn()

    def checkpass(self):
        """パスかどうか判定"""
        if len(rc.get_puttable_points(self.board, self.turn)) > 0:
            return False
        return True

    def is_game_set(self):
        """ ゲームセットか返す　"""
        return rc.is_game_set(self.board)

    def is_my_turn(self, color):
        """ 自分のターンか返す """
        if self.turn == color:
            return True
        return False

'''
class CustomReversiBoard(ReversiBoard):
    """ 途中状態の盤面を作る用のクラス """
    def __init__(self, board, turn):
        self.board = board
        self.turn = turn
'''