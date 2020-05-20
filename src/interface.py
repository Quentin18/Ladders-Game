import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno, showwarning
from src.colors import Colors
from src.player import Player, Players


class FramePlayer:
    """Manage the frame of a player for the interface"""
    def __init__(self, window, num_player):
        self.window = window
        self.num_player = num_player
        self.frame = ttk.LabelFrame(
            self.window, text="Player " + str(num_player))

        # Name
        self.name = tk.StringVar()
        self.name.set("Name")
        self.entry = tk.Entry(self.frame, textvariable=self.name, width=20)
        self.entry.grid(row=0, column=0, padx=10, pady=5)

        # Color
        ttk.Label(self.frame, text="Color").grid(
            row=0, column=1, padx=5, pady=5)
        self.combobox = ttk.Combobox(
            self.frame, values=list(Colors.colors.keys()), state="readonly")
        self.combobox.grid(row=0, column=2, padx=5, pady=5)

        # Auto
        self.auto = tk.StringVar()
        self.auto.set(False)
        self.checkbutton = tk.Checkbutton(
            self.frame, text="Auto", variable=self.auto,
            onvalue=True, offvalue=False)
        self.checkbutton.grid(row=0, column=3, padx=10, pady=5)

        self.frame.pack(fill="x", padx=10, pady=5)

    def get_values(self):
        """Get the values of the frame"""
        name = self.name.get()
        color = self.combobox.get()
        auto = self.auto.get()
        return name, color, auto

    def destroy(self):
        """Destroy a frame"""
        self.frame.destroy()


class Interface:
    """Manage the tkinter interface for choosing the players settings"""
    def __init__(self, window, theme='clam'):
        self.window = window
        self.window.title("Ladders Game")
        self.window.resizable(width=False, height=False)
        self.style = ttk.Style()
        if theme in self.style.theme_names():
            self.style.theme_use(theme)
        self.label = ttk.Label(
            self.window,
            text="Welcome to the Ladders Game! Create the players and valid!")
        self.label.pack(padx=20, pady=10)
        ttk.Button(self.window, text="Add player", width=30,
                   command=self.add_player).pack()
        ttk.Button(self.window, text="Delete player", width=30,
                   command=self.delete_player).pack()
        ttk.Button(self.window, text="Valid", width=30,
                   command=self.valid).pack()
        ttk.Button(self.window, text="Quit", width=30,
                   command=self.close).pack()
        self.frames = [FramePlayer(self.window, i) for i in range(1, 4)]
        self.players = Players()
        self.ready = False

    def get_nb_players(self):
        """Get the number of players"""
        return len(self.frames)

    def add_player(self):
        """Add a player"""
        num = self.get_nb_players()
        if num < 10:
            self.frames.append(FramePlayer(self.window, num + 1))

    def delete_player(self):
        """Delete a player"""
        num = self.get_nb_players()
        if num > 2:
            self.frames[-1].destroy()
            self.frames.pop(-1)

    def check(self):
        """Check the values"""
        names, colors = [], []
        for frame in self.frames:
            name, color, _ = frame.get_values()
            n = len(names) + 1
            if name == '':
                showwarning(
                    "Error",
                    f"The player {n} does not have a name!")
                return False
            if name in names:
                i = names.index(name) + 1
                showwarning(
                    "Error",
                    f"The players {i} and {n} have the same name!")
                return False
            if color == '':
                showwarning(
                    "Error",
                    f"The player {n} does not have a color!")
                return False
            if color in colors:
                i = colors.index(color) + 1
                showwarning(
                    "Error",
                    f"The players {i} and {n} have the same color!")
                return False
            names.append(name)
            colors.append(color)
        return True

    def valid(self):
        """Valid the choices"""
        if self.check():
            for frame in self.frames:
                name, color, auto = frame.get_values()
                self.players.append(
                    Player(name, color, int(auto) == 1))
            self.window.destroy()
            self.ready = True

    def close(self):
        """Close the window"""
        if askyesno("Close", "Are you sure?"):
            self.window.destroy()
