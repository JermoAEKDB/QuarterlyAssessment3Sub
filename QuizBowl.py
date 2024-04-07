import tkinter as tk
import sqlite3

class QuizDatabase:
    def __init__(self, db_name='quiz_questions.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
    
    def fetch_questions(self, category):
        self.cursor.execute("SELECT question, options, answer, feedback_correct, feedback_incorrect FROM questions WHERE category=?", (category,))
        questions = self.cursor.fetchall()
        return questions
    
    def close_connection(self):
        self.conn.close()

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.db = QuizDatabase()

        self.root.title("Quiz App")

        self.category_frame = tk.Frame(self.root)
        self.category_frame.pack()

        self.category_label = tk.Label(self.category_frame, text="Select a category:")
        self.category_label.grid(row=0, column=0, padx=10, pady=10)

        self.categories = ["Handgun Familiarity & Safety", "American Literature", "Database Management", "Programming Logic & Analytic Thinking", "Topics in British Literature"]
        self.selected_category = tk.StringVar()
        self.selected_category.set(self.categories[0])

        self.category_menu = tk.OptionMenu(self.category_frame, self.selected_category, *self.categories)
        self.category_menu.grid(row=0, column=1, padx=10, pady=10)

        self.start_button = tk.Button(self.category_frame, text="Start Quiz", command=self.start_quiz)
        self.start_button.grid(row=1, columnspan=2, padx=10, pady=10)

    def start_quiz(self):
        selected_category = self.selected_category.get()
        self.questions = self.db.fetch_questions(selected_category)

        self.category_frame.destroy()

        self.quiz_frame = tk.Frame(self.root)
        self.quiz_frame.pack()

        self.question_index = 0

        self.question_label = tk.Label(self.quiz_frame, text=self.questions[self.question_index][0])
        self.question_label.pack(pady=10)

        self.options = self.questions[self.question_index][1].split("\n")
        self.selected_option = tk.StringVar()
        self.selected_option.set("")

        for option in self.options:
            tk.Radiobutton(self.quiz_frame, text=option, variable=self.selected_option, value=option).pack()

        self.submit_button = tk.Button(self.quiz_frame, text="Submit", command=self.submit_answer)
        self.submit_button.pack(pady=10)

    def submit_answer(self):
        selected_option = self.selected_option.get()
        correct_answer = self.questions[self.question_index][2].strip()

        
        selected_option_cleaned = selected_option.strip().lower() if selected_option else ""
        correct_answer_cleaned = correct_answer.strip().lower()

        feedback = self.questions[self.question_index][3] if selected_option_cleaned == correct_answer_cleaned else self.questions[self.question_index][4]
        color = "green" if selected_option_cleaned == correct_answer_cleaned else "red"

        self.feedback_label = tk.Label(self.quiz_frame, text=feedback, fg=color)
        self.feedback_label.pack(pady=10)

        self.question_index += 1
        if self.question_index < len(self.questions):
            self.question_label.config(text=self.questions[self.question_index][0])
            self.options = self.questions[self.question_index][1].split("\n")
            self.selected_option.set("")
            for widget in self.quiz_frame.winfo_children():
                if isinstance(widget, tk.Radiobutton):
                    widget.destroy()
            for option in self.options:
                tk.Radiobutton(self.quiz_frame, text=option, variable=self.selected_option, value=option).pack()
        else:
            self.quiz_frame.destroy()
            tk.Label(self.root, text="Quiz Completed!").pack()


root = tk.Tk()
app = QuizApp(root)
root.mainloop()
