import pygame
from src.data import Sounds


class Pawn:
    """Manage a pawn"""
    def __init__(self, color, board, radius=10, case=1, vel=2):
        self.color = color
        self.board = board
        self.radius = radius
        self.case = case
        self.vel = vel
        self.x, self.y = board.get_coords(case)

    def reset(self):
        """Reset a pawn"""
        self.case = 1
        self.x, self.y = self.board.get_coords(1)

    def draw(self):
        """Draw a pawn"""
        pygame.draw.circle(self.board.screen, self.color, [self.x, self.y],
                           self.radius)

    def move_box(self, start_line, gt100, dice, turn,
                 finished, current_p, players):
        """Move a pawn in the boxes"""
        x_end, y_end = self.board.get_coords(self.case)
        if start_line % 2 == 0:
            orient = -1
            limit = self.board.coords[1][0] + int(self.board.case_side / 2)
            run = False
        else:
            orient = 1
            limit = self.board.coords[10][0] + int(self.board.case_side / 2)
            run = True
        if y_end != self.y or gt100:
            while not self.x == limit:
                if ((run and self.x + self.vel > limit)
                        or ((not run) and self.x - self.vel < limit)):
                    self.x = limit
                else:
                    self.x += self.vel * orient
                self.board.redraw(turn, finished, current_p, players)
            while not self.y == y_end:
                if self.y - self.vel < y_end:
                    self.y = y_end
                else:
                    self.y -= self.vel
                self.board.redraw(turn, finished, current_p, players)
            orient *= -1
            run = not run
        while not self.x == x_end:
            if ((run and self.x + self.vel > x_end)
                    or ((not run) and self.x - self.vel < x_end)):
                self.x = x_end
            else:
                self.x += self.vel * orient
            self.board.redraw(turn, finished, current_p, players)

    def move_ladder(self, dice, turn, finished, current_p, players):
        """Move a pawn in a ladder"""
        x_end, y_end = self.board.get_coords(self.case)
        if x_end >= self.x:
            orient_x = 1
            run_x = True
        else:
            orient_x = -1
            run_x = False
        if y_end >= self.y:
            orient_y = 1
            run_y = True
        else:
            orient_y = -1
            run_y = False
        vel_x = round(abs(x_end - self.x) / 100)
        vel_y = round(abs(y_end - self.y) / 100)
        while not (self.x == x_end and self.y == y_end):
            if self.x != x_end:
                if ((run_x and self.x + vel_x > x_end)
                        or ((not run_x) and self.x - vel_x < x_end)):
                    self.x = x_end
                else:
                    self.x += vel_x * orient_x
            if self.y != y_end:
                if ((run_y and self.y + vel_y > y_end)
                        or ((not run_y) and self.y - vel_y < y_end)):
                    self.y = y_end
                else:
                    self.y += vel_y * orient_y
            self.board.redraw(turn, finished, current_p, players)

    def move(self, dice, turn, finished, current_p, players):
        """Move a pawn"""
        gt100 = False
        start_line = self.board.get_line(self.case)
        self.case += dice
        if self.case > 100:
            self.case = 100 - (self.case - 100)
            gt100 = True
        self.move_box(
            start_line, gt100, dice, turn, finished, current_p, players)
        for key in self.board.ladders.dict:
            if key == self.case:
                if self.case < self.board.ladders.dict[key]:
                    Sounds.mario.play()
                else:
                    Sounds.looser.play()
                self.case = self.board.ladders.dict[key]
                self.move_ladder(dice, turn, finished, current_p, players)
                break
        return self.case
