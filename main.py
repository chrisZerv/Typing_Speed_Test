import tkinter as tk
from tkinter import messagebox
import time
import random

# Sample texts to type
sample_texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an interpreted, high-level, general-purpose programming language.",
    "Tkinter is the standard GUI library for Python.",
    "Typing speed tests are a great way to improve your typing skills.",
    "The best way to learn programming is by practicing with small projects."
]

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("600x400")
        self.root.config(bg="#f7f7f7")

        self.sample_text = random.choice(sample_texts)
        self.start_time = None
        self.high_score = 0

        # Title Label
        self.title_label = tk.Label(root, text="Typing Speed Test", font=("Helvetica", 24, "bold"), bg="#f7f7f7", fg="#333")
        self.title_label.pack(pady=20)

        # Sample Text Display
        self.sample_label = tk.Label(root, text=self.sample_text, wraplength=500, font=("Arial", 14), bg="#ffffff", fg="#000", bd=2, relief="solid", padx=10, pady=10)
        self.sample_label.pack(pady=20)

        # Typing Entry
        self.typing_entry = tk.Entry(root, width=60, font=("Arial", 14), bd=2, relief="solid", bg="#e6e6e6")
        self.typing_entry.pack(pady=20)
        self.typing_entry.bind("<KeyRelease>", self.start_test)

        # WPM Display
        self.wpm_label = tk.Label(root, text="WPM: 0", font=("Arial", 16, "bold"), bg="#f7f7f7", fg="#007acc")
        self.wpm_label.pack(pady=10)

        # High Score Display
        self.high_score_label = tk.Label(root, text=f"High Score: {self.high_score} WPM", font=("Arial", 16, "bold"), bg="#f7f7f7", fg="#d9534f")
        self.high_score_label.pack(pady=10)

        # Reset Button
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_test, font=("Arial", 14, "bold"), bg="#5bc0de", fg="#ffffff", width=10, bd=0, relief="solid")
        self.reset_button.pack(pady=20)

    def start_test(self, event):
        if not self.start_time:
            self.start_time = time.time()
        if self.typing_entry.get() == self.sample_text:
            self.calculate_wpm()

    def calculate_wpm(self):
        elapsed_time = time.time() - self.start_time
        word_count = len(self.sample_text.split())
        wpm = word_count / (elapsed_time / 60)
        self.wpm_label.config(text=f"WPM: {int(wpm)}")

        if wpm > self.high_score:
            self.high_score = int(wpm)
            self.high_score_label.config(text=f"High Score: {self.high_score} WPM")

        messagebox.showinfo("Typing Speed Test", f"Your typing speed is {int(wpm)} WPM.")
        self.reset_test()

    def reset_test(self):
        self.start_time = None
        self.typing_entry.delete(0, tk.END)
        self.sample_text = random.choice(sample_texts)
        self.sample_label.config(text=self.sample_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()
