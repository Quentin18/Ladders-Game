import tkinter as tk
import pygame
from src.interface import Interface
from src.board import Board
from src.ladder import Ladders
from src.pawn import Pawn
from src.data import Sounds


# Interface
window = tk.Tk()
i = Interface(window)
window.mainloop()

# Game
if i.ready:
    players = i.players
    # print(players)

    # Ladders
    ladders = Ladders()
    for start, end in zip(
        [5, 8, 14, 19, 25, 39, 47, 49, 58, 62, 68, 74, 84],
            [24, 50, 48, 44, 56, 60, 75, 90, 77, 98, 92, 95, 96]):
        ladders.append(start, end)

    # Board
    b = Board(ladders)

    # Pawns
    for p in players.players:
        p.pawn = Pawn(p.color, b)

    turn = 1
    run = True
    finished = False
    clock = pygame.time.Clock()
    current_p = 0

    while run:
        clock.tick(40)
        b.redraw(turn, finished, current_p, players)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        # Game
        if not finished:
            p = players.players[current_p]
            if p.auto or keys[pygame.K_SPACE]:
                dice = b.roll_dice()
                p.play(dice, turn, finished, current_p, players)
                if p.win():
                    finished = True
                    Sounds.winning.play()
                else:
                    current_p = (current_p + 1) % players.nb
                    if current_p == 0:
                        turn += 1

        # Game is not running
        else:
            if keys[pygame.K_SPACE]:
                finished = False
                current_p = 0
                turn = 1
                players.reset()

        # Stats
        if keys[pygame.K_s]:
            players.show_stats()

    pygame.quit()
