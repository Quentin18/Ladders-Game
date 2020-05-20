import pygame
import time
from random import randint
from src.colors import Colors
from src.data import Dice


class Board:
    """Manage the board game"""
    def __init__(self, ladders, side=700):
        pygame.init()
        self.side = side
        self.case_side = int(side / 10)
        self.size = [side + 210, side]
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Ladders Game")
        self.font = pygame.font.SysFont('consolas', 18)
        self.coords = self.make_coords()
        self.ladders = ladders

    def make_coords(self):
        """
        Make the coords dictionnary
        keys -> num
        values -> pos (x, y)
        """
        coords = {}
        num = 100
        step = -1
        for y in range(0, self.side, self.case_side):
            for x in range(0, self.side, self.case_side):
                coords[num] = (x, y)
                if x < self.side - self.case_side:
                    num += step
            num -= 10
            step *= -1
        return coords

    def get_coords(self, case):
        """Return the coords of a case"""
        return [self.coords[case][0] + int(self.case_side / 2),
                self.coords[case][1] + int(self.case_side / 2)]

    def get_line(self, case):
        """Get the line number of a case"""
        if case < 11:
            return 1
        elif case < 21:
            return 2
        elif case < 31:
            return 3
        elif case < 41:
            return 4
        elif case < 51:
            return 5
        elif case < 61:
            return 6
        elif case < 71:
            return 7
        elif case < 81:
            return 8
        elif case < 91:
            return 9
        else:
            return 10

    def draw_grid(self):
        """Draw the grid"""
        for x in range(0, self.side + self.case_side, self.case_side):
            pygame.draw.line(self.screen, Colors.red, [x, 0], [x, self.side])
        for y in range(self.case_side, self.side + self.case_side,
                       self.case_side):
            if y % (self.case_side * 2) == 0:
                pygame.draw.line(
                    self.screen, Colors.red, [0, y], [self.case_side, y])
                pygame.draw.line(
                    self.screen, Colors.blue, [self.case_side, y],
                    [self.side, y], 5)
            else:
                pygame.draw.line(
                    self.screen, Colors.blue, [0, y],
                    [self.side - self.case_side, y], 5)
                pygame.draw.line(
                    self.screen, Colors.red, [self.side - self.case_side, y],
                    [self.side, y])
        pygame.draw.rect(
            self.screen, Colors.blue, [0, 0, self.side, self.side], 5)

    def draw_nums(self):
        """Draw the num of the cases"""
        num = 100
        step = -1
        for y in range(self.case_side - 15, self.side, self.case_side):
            for x in range(18, self.side, self.case_side):
                text = self.font.render(
                    str(num), True, Colors.white, Colors.black)
                text_rect = text.get_rect()
                text_rect.center = (x, y)
                self.screen.blit(text, text_rect)
                if x < self.side - self.case_side:
                    num += step
            num -= 10
            step *= -1

    def draw_info(self, turn, finished, current_p, players):
        """Draw the informations on the right"""
        if not finished:
            state_p = " plays!"
            action = " to roll the dice!"
        else:
            state_p = " wins!"
            action = " to replay!"
        text_action = self.font.render("Press SPACE" + action, 1, Colors.black)
        self.screen.blit(text_action, (self.side + 10, 400))
        text_turn = self.font.render("Turn n° " + str(turn), 1, Colors.black)
        self.screen.blit(text_turn, (self.side + 10, 490))
        text_stat = self.font.render("Stats : press s", 1, Colors.black)
        self.screen.blit(text_stat, (self.side + 10, 520))
        p = players.players[current_p]
        text_player = self.font.render(p.name + state_p, 1, p.color)
        self.screen.blit(text_player, (self.side + 10, 300))

    def redraw(self, turn, finished, current_p, players):
        """Redraw the window"""
        self.screen.fill(Colors.white)
        self.draw_grid()
        self.ladders.draw(self)
        self.draw_nums()
        for p in players.players:
            p.pawn.draw()
        self.draw_info(turn, finished, current_p, players)
        pygame.display.update()

    def roll_dice(self):
        """
        Roll the dice, show the number on the screen, and return the number
        """
        choice = randint(1, 6)
        self.screen.blit(Dice.image[choice - 1], (self.side + 3, 0))
        pygame.display.update()
        time.sleep(1)
        return choice
