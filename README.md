# Ladders Game

The **Ladders Game** is a variation of the game *[Snakes and Ladders](https://en.wikipedia.org/wiki/Snakes_and_Ladders)* with Python and pygame. A very funny game for 2 to 10 players with sounds effects!
![](https://github.com/Quentin18/Ladders-Game/blob/master/captures/game.png)

## Rules
The object of the game is to be the first player to reach the end by moving across the board from square one to the final square.
- The players will move their pieces from left to right, starting at 1, following the numbers on the board, then the next row from right to left and repeat.
- Roll the dice. Move your piece the number of spaces shown on the dice.
- If your piece arrives at the bottom of a ladder, you move up to the top of the ladder.
- If your piece arrives at the top of a ladder, you move up to the bottom of the ladder.
- To win, you need to roll the exact number to reach the final square. If the die roll is too large, you need to bounce back.

## Install
To install, open a command prompt and launch:
```bash
git clone https://github.com/Quentin18/Ladders-Game.git
```

You need to install [pygame](https://www.pygame.org/news) and [matplotlib](https://matplotlib.org/3.1.1/index.html):
```bash
pip3 install pygame
pip3 install matplotlib
```

## Play
This is how to launch the Ladders Game:
1. Go in the directory:
```bash
cd Ladders-Game
```
2. Launch the **main** file:
```bash
python3 main.py
```
3. You arrive in a tkinter window to create the players. The checkbutton **Auto** means that you don't have to press SPACE to roll the dice if it is checked.

![](https://github.com/Quentin18/Ladders-Game/blob/master/captures/tkinter.png)
4. Click on **Valid** and the game starts.

## Stats
If you press **s**, you can see the evolution of the game thanks to matplotlib.
![](https://github.com/Quentin18/Ladders-Game/blob/master/captures/stats.png)

## Contact
quentindeschamps18@gmail.com

## License
[MIT](https://choosealicense.com/licenses/mit/)
