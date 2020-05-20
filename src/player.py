try:
    import matplotlib.pyplot as plt
except Exception:
    print("Install matplotlib to get stats")
from src.colors import Colors


class Player:
    """Manage a player"""
    def __init__(self, name, color, auto):
        self.name = name
        self.color_name = color
        self.color = Colors.colors[color]
        self.auto = auto
        self.pawn = None
        self.stats = [1]

    def __str__(self):
        """Return the informations of a player"""
        return ", ".join([self.name, self.color_name, str(self.auto)])

    def reset(self):
        """Reset a player"""
        self.stats = [1]
        self.pawn.reset()

    def win(self):
        """Return True if the player wins"""
        return self.pawn.case == 100

    def play(self, dice, turn, finished, current_p, players):
        """Make the player play"""
        case = self.pawn.move(dice, turn, finished, current_p, players)
        self.stats.append(case)


class Players:
    """Manage the players"""
    def __init__(self):
        self.nb = 0
        self.players = []

    def append(self, player):
        """Add a player"""
        self.nb += 1
        self.players.append(player)

    def __str__(self):
        """Return the informations of the players"""
        return "\n".join([str(p) for p in self.players])

    def reset(self):
        """Reset all players"""
        for p in self.players:
            p.reset()

    def show_stats(self):
        """Show the stats"""
        try:
            for p in self.players:
                plt.plot(p.stats, label=p.name, color=p.color_name)
            plt.title("Evolution of the game")
            plt.xlabel("Turn")
            plt.ylabel("Case")
            plt.legend()
            plt.show()
        except Exception:
            print("Install matplotlib to get stats")
