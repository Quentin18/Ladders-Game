import pygame
from src.colors import Colors


class Ladder:
    """Manage a ladder"""
    def __init__(self, start, end, color=Colors.brown):
        self.start = start
        self.end = end
        self.color = color

    def draw(self, board):
        """Draw a ladder"""
        start_pos1 = (
            board.coords[self.start][0] + 5,
            board.coords[self.start][1] + int(board.case_side / 2))
        end_pos1 = (
            board.coords[self.end][0] + 5,
            board.coords[self.end][1] + int(board.case_side / 2))
        start_pos2 = (
            board.coords[self.start][0] + board.case_side - 5,
            board.coords[self.start][1] + int(board.case_side / 2))
        end_pos2 = (
            board.coords[self.end][0] + board.case_side - 5,
            board.coords[self.end][1] + int(board.case_side / 2))
        pygame.draw.line(board.screen, self.color, start_pos1, end_pos1, 5)
        pygame.draw.line(board.screen, self.color, start_pos2, end_pos2, 5)


class Ladders:
    """Manage the ladders"""
    def __init__(self):
        self.ladders = []
        self.dict = {}

    def append(self, start, end, color=Colors.brown):
        """Add a ladder"""
        self.ladders.append(Ladder(start, end, color))
        if start not in self.dict:
            self.dict[start] = end
        else:
            raise Exception("You can't have two ladders on the same case")
        if end not in self.dict:
            self.dict[end] = start
        else:
            raise Exception("You can't have two ladders on the same case")

    def draw(self, board):
        """Draw the ladders on the game board"""
        for ladder in self.ladders:
            ladder.draw(board)
