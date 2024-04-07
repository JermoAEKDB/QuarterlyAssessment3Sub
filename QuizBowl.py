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
