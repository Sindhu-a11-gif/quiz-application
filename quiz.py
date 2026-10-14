import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "question": "What does CPU stand for?",
        "options": ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Core Processing Unit"],
        "answer": "Central Processing Unit"
    },
    {
        "question": "Which language is used for web styling?",
        "options": ["Python", "Java", "CSS", "C++"],
        "answer": "CSS"
    },
    {
        "question": "What is the output of 2 ** 3 in Python?",
        "options": ["6", "9", "8", "5"],
        "answer": "8"
    },
    {
        "question": "Which data structure uses LIFO order?",
        "options": ["Queue", "Stack", "Array", "Linked List"],
        "answer": "Stack"
    },
    {
        "question": "What does RAM stand for?",
        "options": ["Random Access Memory", "Read Access Mode", "Run All Memory", "Random Array Module"],
        "answer": "Random Access Memory"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("600x400")
        self.root.config(bg="#f0f4f8")

        self.index = 0
        self.score = 0
        self.selected = tk.StringVar()

        # Question number label
        self.q_number = tk.Label(root, text="", bg="#f0f4f8", font=("Arial", 11), fg="#888")
        self.q_number.pack(pady=(30, 0))

        # Question label
        self.q_label = tk.Label(root, text="", bg="#f0f4f8", font=("Arial", 14, "bold"),
                                 wraplength=520, justify="center", fg="#222")
        self.q_label.pack(pady=(10, 20))

        # Options frame
        self.options_frame = tk.Frame(root, bg="#f0f4f8")
        self.options_frame.pack()

        self.option_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(
                self.options_frame,
                text="",
                variable=self.selected,
                value="",
                bg="#f0f4f8",
                font=("Arial", 12),
                fg="#333",
                activebackground="#f0f4f8",
                selectcolor="#d0e8ff",
                anchor="w"
            )
            btn.pack(fill="x", padx=60, pady=4)
            self.option_buttons.append(btn)

        # Next button
        self.next_btn = tk.Button(root, text="Next →", command=self.next_question,
                                   bg="#4A90D9", fg="white", font=("Arial", 12, "bold"),
                                   padx=20, pady=6, relief="flat", cursor="hand2")
        self.next_btn.pack(pady=30)

        self.load_question()

    def load_question(self):
        self.selected.set(None)
        q = questions[self.index]
        self.q_number.config(text=f"Question {self.index + 1} of {len(questions)}")
        self.q_label.config(text=q["question"])
        for i, btn in enumerate(self.option_buttons):
            btn.config(text=q["options"][i], value=q["options"][i])

        if self.index == len(questions) - 1:
            self.next_btn.config(text="Submit ✓")

    def next_question(self):
        answer = self.selected.get()
        if not answer or answer == "None":
            messagebox.showwarning("No answer", "Please select an answer before continuing!")
            return

        if answer == questions[self.index]["answer"]:
            self.score += 1

        self.index += 1

        if self.index < len(questions):
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        total = len(questions)
        percent = (self.score / total) * 100

        tk.Label(self.root, text="Quiz Complete!", bg="#f0f4f8",
                 font=("Arial", 20, "bold"), fg="#222").pack(pady=(60, 10))

        tk.Label(self.root, text=f"Your Score: {self.score} / {total}",
                 bg="#f0f4f8", font=("Arial", 16), fg="#4A90D9").pack(pady=5)

        if percent == 100:
            msg = "🎉 Perfect score! Excellent!"
        elif percent >= 60:
            msg = "👍 Good job! Keep it up!"
        else:
            msg = "📖 Keep practicing, you'll get there!"

        tk.Label(self.root, text=msg, bg="#f0f4f8", font=("Arial", 13), fg="#555").pack(pady=10)

        tk.Button(self.root, text="Play Again", command=self.restart,
                  bg="#4A90D9", fg="white", font=("Arial", 12, "bold"),
                  padx=20, pady=6, relief="flat", cursor="hand2").pack(pady=30)

    def restart(self):
        self.index = 0
        self.score = 0
        for widget in self.root.winfo_children():
            widget.destroy()
        self.__init__(self.root)

root = tk.Tk()
app = QuizApp(root)
root.mainloop()