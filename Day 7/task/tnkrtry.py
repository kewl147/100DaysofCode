# hangman_gui.py
import random
import string
import tkinter as tk
from tkinter import messagebox

# If you split words/art into modules, import here:
from hangman_words import word_list

# Simple stick-figure parts to draw on a Canvas
def draw_gallows(c):
    c.create_line(20, 180, 180, 180, width=3)   # base
    c.create_line(60, 180, 60, 20, width=3)     # post
    c.create_line(60, 20, 130, 20, width=3)     # beam
    c.create_line(130, 20, 130, 40, width=3)    # rope

def draw_part(c, lives_left):
    # lives start at 6; each wrong guess draws one new part
    parts = [
        lambda: c.create_oval(115, 40, 145, 70, width=3),                # head
        lambda: c.create_line(130, 70, 130, 110, width=3),               # body
        lambda: c.create_line(130, 80, 110, 95, width=3),                # left arm
        lambda: c.create_line(130, 80, 150, 95, width=3),                # right arm
        lambda: c.create_line(130, 110, 115, 135, width=3),              # left leg
        lambda: c.create_line(130, 110, 145, 135, width=3),              # right leg
    ]
    # draw according to how many were lost already
    drawn = 6 - lives_left
    if 1 <= drawn <= len(parts):
        parts[drawn-1]()

class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman")
        self.root.resizable(False, False)  # no resizing = no scrolling

        # Layout
        self.canvas = tk.Canvas(root, width=200, height=200, bg="white", highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        draw_gallows(self.canvas)

        self.word_var = tk.StringVar()
        self.info_var = tk.StringVar(value="Guess a letter.")
        self.lives_var = tk.StringVar()

        tk.Label(root, textvariable=self.word_var, font=("Courier New", 20)).grid(row=1, column=0, columnspan=3, pady=(0,10))
        tk.Label(root, textvariable=self.info_var).grid(row=2, column=0, columnspan=3)
        tk.Label(root, textvariable=self.lives_var).grid(row=3, column=0, columnspan=3, pady=(0,10))

        # Letter buttons
        self.buttons = {}
        letters_frame = tk.Frame(root)
        letters_frame.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
        for idx, ch in enumerate(string.ascii_lowercase):
            btn = tk.Button(letters_frame, text=ch.upper(), width=3, command=lambda c=ch: self.guess(c))
            btn.grid(row=idx//9, column=idx%9, padx=2, pady=2)
            self.buttons[ch] = btn

        # Control buttons
        tk.Button(root, text="New Game", command=self.new_game).grid(row=5, column=0, pady=10)
        tk.Button(root, text="Quit", command=root.destroy).grid(row=5, column=2, pady=10)

        self.new_game()

    def new_game(self):
        self.chosen_word = random.choice(word_list)
        self.display = ["_"] * len(self.chosen_word)
        self.lives = 6  # matches the 6 body parts
        self.guessed = set()
        self.canvas.delete("all")
        draw_gallows(self.canvas)
        for b in self.buttons.values():
            b.config(state=tk.NORMAL)
        self.update_labels("New game! Guess a letter.")

    def update_labels(self, info=""):
        self.word_var.set(" ".join(self.display))
        self.lives_var.set(f"Lives: {self.lives}")
        if info:
            self.info_var.set(info)

    def end_game(self, win: bool):
        for b in self.buttons.values():
            b.config(state=tk.DISABLED)
        if win:
            self.update_labels(f"You win! The word was '{self.chosen_word}'.")
            messagebox.showinfo("You win!", f"🎉 You guessed '{self.chosen_word}'!")
        else:
            # reveal word
            self.display = list(self.chosen_word)
            self.update_labels(f"You lose! The word was '{self.chosen_word}'.")
            messagebox.showinfo("Game over", f"💀 The word was '{self.chosen_word}'.")

    def guess(self, ch):
        if ch in self.guessed or self.lives == 0:
            return
        self.guessed.add(ch)
        # Disable button to prevent repeats
        self.buttons[ch].config(state=tk.DISABLED)

        if ch in self.chosen_word:
            for i, letter in enumerate(self.chosen_word):
                if letter == ch:
                    self.display[i] = ch
            self.update_labels(f"Correct: {ch.upper()}")
            if "_" not in self.display:
                self.end_game(True)
        else:
            self.lives -= 1
            draw_part(self.canvas, self.lives)
            self.update_labels(f"Incorrect: {ch.upper()}")
            if self.lives == 0:
                self.end_game(False)

if __name__ == "__main__":
    root = tk.Tk()
    HangmanGUI(root)
    root.mainloop()
