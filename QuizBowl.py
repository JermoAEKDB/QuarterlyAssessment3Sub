import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3
import random

class QuizApp:
    def __init__(self):
        self.db_name = 'quiz_questions.db'
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.categories = self.get_categories()
        self.score = 0

    def get_categories(self):
        self.cursor.execute("SELECT DISTINCT category FROM questions")
        return [row[0] for row in self.cursor.fetchall()]

    def start(self):
        self.main_window()

    def main_window(self):
        self.root = tk.Tk()
        self.root.title("Select Quiz Category")

        self.root.geometry("400x200")  # Set window width and height
        self.center_window(self.root)

        tk.Label(self.root, text="Select Category:").pack()
        self.category_var = tk.StringVar(self.root)
        self.category_var.set(self.categories[0])  # Default to first category
        tk.OptionMenu(self.root, self.category_var, *self.categories).pack()

        tk.Button(self.root, text="Start Quiz Now", command=self.start_quiz).pack()

        self.root.mainloop()

    def start_quiz(self):
        selected_category = self.category_var.get()
        questions = self.get_questions(selected_category)
        if not questions:
            messagebox.showerror("Error", "No questions found for selected category")
            return
        self.quiz_window(questions)

    def get_questions(self, category):
        self.cursor.execute("SELECT * FROM questions WHERE category=?", (category,))
        return self.cursor.fetchall()

    def quiz_window(self, questions):
        self.root.destroy()  # Close main window

        self.quiz_root = tk.Tk()
        self.quiz_root.title("Quiz")

        self.quiz_root.geometry("800x400")  # Set window width and height
        self.center_window(self.quiz_root)

        self.current_question = 0
        self.questions = questions
        random.shuffle(self.questions)

        self.display_question()

        self.quiz_root.mainloop()

    def display_question(self):
        self.quiz_root.destroy()  # Destroy previous question window if exists
        self.quiz_root = tk.Tk()
        self.quiz_root.title("Question {}".format(self.current_question + 1))

        self.quiz_root.geometry("800x400")  # Set window width and height
        self.center_window(self.quiz_root)

        question = self.questions[self.current_question]
        tk.Label(self.quiz_root, text=question[2], wraplength=700).pack()  # Display question with wrapping

        if question[3] == "MCQ":
            options = question[4].split("\n")
            tk.Label(self.quiz_root, text="Answer Choices: " + ", ".join(options)).pack()
            self.mcq_answer = tk.StringVar()
            entry_frame = tk.Frame(self.quiz_root)
            entry_frame.pack()
            tk.Label(entry_frame, text="Your Answer:").pack(side=tk.LEFT)
            tk.Entry(entry_frame, textvariable=self.mcq_answer, width=5).pack(side=tk.LEFT)
        elif question[3] == "True/False":
            tk.Label(self.quiz_root, text="True/False: True or False").pack()
            self.tf_answer = tk.StringVar()
            entry_frame = tk.Frame(self.quiz_root)
            entry_frame.pack()
            tk.Label(entry_frame, text="Your Answer:").pack(side=tk.LEFT)
            tk.Entry(entry_frame, textvariable=self.tf_answer, width=5).pack(side=tk.LEFT)
        elif question[3] == "Short Answer":
            self.sa_answer = tk.StringVar()
            tk.Entry(self.quiz_root, textvariable=self.sa_answer).pack()

        submit_button = tk.Button(self.quiz_root, text="Submit Answer", command=self.submit_answer)
        submit_button.pack()

    def submit_answer(self):
        question = self.questions[self.current_question]
        correct_answer = question[5]

        if question[3] == "MCQ":
            selected_answer = self.mcq_answer.get().upper()
            if selected_answer == correct_answer:
                self.score += 1
                feedback = "Your answer is correct!"
                color = "green"
            else:
                feedback = "Your answer is incorrect. Correct answer is: {}".format(correct_answer)
                color = "red"
        elif question[3] == "True/False":
            selected_answer = self.tf_answer.get().lower()
            if selected_answer == correct_answer.lower():
                self.score += 1
                feedback = "Your answer is correct!"
                color = "green"
            else:
                feedback = "Your answer is incorrect. Correct answer is: {}".format(correct_answer)
                color = "red"
        elif question[3] == "Short Answer":
            selected_answer = self.sa_answer.get().lower()
            if selected_answer == correct_answer.lower():
                self.score += 1
                feedback = "Your answer is correct!"
                color = "green"
            else:
                feedback = "Your answer is incorrect. Correct answer is: {}".format(correct_answer)
                color = "red"

        feedback_label = tk.Label(self.quiz_root, text=feedback, fg=color)
        feedback_label.pack()

        self.current_question += 1
        if self.current_question < len(self.questions):
            next_button = tk.Button(self.quiz_root, text="Next Question", command=self.display_question)
            next_button.pack()
        else:
            self.show_scoreboard()

    def show_scoreboard(self):
        self.quiz_root.destroy()  # Destroy quiz window

        scoreboard_root = tk.Tk()
        scoreboard_root.title("Quiz Scoreboard")

        self.center_window(scoreboard_root)

        tk.Label(scoreboard_root, text="Quiz Complete! Your Score: {}/{}".format(self.score, len(self.questions))).pack()

        scoreboard_root.mainloop()

    def center_window(self, window):
        window.update_idletasks()
        width = window.winfo_reqwidth() + 600  # Add extra width
        height = window.winfo_reqheight()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

if __name__ == "__main__":
    quiz_app = QuizApp()
    quiz_app.start()
