import tkinter as tk
from tkinter import messagebox
import sqlite3
import random

class QuizDatabase:
    def __init__(self, db_name='quiz_questions.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
    
    def get_questions_by_category(self, category):
        self.cursor.execute('''SELECT question, question_type, options, answer, feedback_correct, feedback_incorrect
                               FROM questions
                               WHERE category = ?''', (category,))
        return self.cursor.fetchall()
    
    def close_connection(self):
        self.conn.close()

class QuizGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.quiz_db = QuizDatabase()
        
        # Creates main window
        self.create_category_selection_window()
        
        self.root.mainloop()
    
    def create_category_selection_window(self):
        self.root.title("Select Category")
        
        # Creates label
        label = tk.Label(self.root, text="Select a category:")
        label.pack()
        
        # Creates the radio buttons for categories
        self.category_var = tk.StringVar()
        categories = ["Handgun Familiarity & Safety", "American Literature", "Database Management", 
                      "Programming Logic & Analytic Thinking", "Topics in British Literature"]
        for category in categories:
            tk.Radiobutton(self.root, text=category, variable=self.category_var, value=category).pack()
        
        # Creates the button to start quiz
        start_button = tk.Button(self.root, text="Start Quiz", command=self.start_quiz)
        start_button.pack()
    
    def start_quiz(self):
        selected_category = self.category_var.get()
        if not selected_category:
            messagebox.showwarning("Warning", "Please select a category.")
            return
        
        # Gets the questions for the selected category
        self.questions = self.quiz_db.get_questions_by_category(selected_category)
        
        # Closes the category selection window
        self.root.destroy()
        
        # Creates the quiz window
        self.create_quiz_window()
    
    def create_quiz_window(self):
        self.quiz_window = tk.Tk()
        self.quiz_window.title("Quiz")
        
        # Displays the questions
        self.current_question_idx = 0
        self.display_question()
        
        self.quiz_window.mainloop()
    
    def display_question(self):
        question, question_type, options, answer, feedback_correct, feedback_incorrect = self.questions[self.current_question_idx]
        
        # Creates the question label
        question_label = tk.Label(self.quiz_window, text=f"Question {self.current_question_idx + 1}: {question}")
        question_label.pack()
        
        # Displays the options
        if question_type == "MCQ":
            options = options.split("\n")
            self.selected_option = tk.StringVar()
            for option in options:
                tk.Radiobutton(self.quiz_window, text=option, variable=self.selected_option, value=option).pack()
        elif question_type == "Short Answer":
            self.answer_entry = tk.Entry(self.quiz_window)
            self.answer_entry.pack()
        
        # Creates the submit button
        submit_button = tk.Button(self.quiz_window, text="Submit", command=self.check_answer)
        submit_button.pack()
    
    def check_answer(self):
        if hasattr(self, 'selected_option'):
            user_answer = self.selected_option.get()
        elif hasattr(self, 'answer_entry'):
            user_answer = self.answer_entry.get()
        
        _, _, _, answer, feedback_correct, feedback_incorrect = self.questions[self.current_question_idx]
        
        if user_answer.strip().lower() == answer.strip().lower():
            messagebox.showinfo("Feedback", feedback_correct)
        else:
            messagebox.showinfo("Feedback", feedback_incorrect)
        
        self.current_question_idx += 1
        if self.current_question_idx < len(self.questions):
            self.clear_question_widgets()
            self.display_question()
        else:
            messagebox.showinfo("Quiz Over", "Quiz completed. Thank you!")
            self.quiz_window.destroy()
            self.quiz_db.close_connection()
    
    def clear_question_widgets(self):
        for widget in self.quiz_window.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    QuizGUI()
