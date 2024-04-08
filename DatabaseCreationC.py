import sqlite3

class QuizDatabase:
    def __init__(self, db_name='quiz_questions.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
    
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS questions (
                             id INTEGER PRIMARY KEY,
                             category TEXT,
                             question TEXT,
                             question_type TEXT,
                             options TEXT,
                             answer TEXT,
                             feedback_correct TEXT,
                             feedback_incorrect TEXT)''')
        self.conn.commit()
    
    def insert_questions(self, questions_data):
        formatted_data = []
        for question in questions_data:
            formatted_options = question[3].replace(",", "\n")  
            formatted_question = (*question[:3], formatted_options, *question[4:])
            formatted_data.append(formatted_question)
        
        self.cursor.executemany('''INSERT INTO questions (category, question, question_type, options, answer, feedback_correct, feedback_incorrect)
                          VALUES (?, ?, ?, ?, ?, ?, ?)''', formatted_data)
        self.conn.commit()
    
    def close_connection(self):
        self.conn.close()

# Sample data of questions for each category
questions_data = [
    # Category 1
    ("Handgun Familiarity & Safety", "What is the heaviest grain of .22 ammunition?", "MCQ", "A) 55 Gr\nB) 60 Gr\nC) 30 Gr\nD) 40 Gr", "B)", "Yes, you are correct as it is the heaviest weight", "This is incorrect as 60 Grain .22 ammo is the heaviest amongst the selections."),
    ("Handgun Familiarity & Safety", "What action for a handgun doesn't require the hammer or release to fire?", "MCQ", "A) Single-Action\nB) Double-Action\nC) Strike-Fire\nD) Single/double-Action","C)","This is correct as a strike-fire handgun doesn't require the hammer or release to be used but a striker.","This is incorrect as the only action for a handgun that doesn't require a hammer or a release is the Strike-Fire action."),
    ("Handgun Familiarity & Safety","Where must a handgun always be pointed at the range?","MCQ","A) Towards the range\nB) Pointed down at your foot\nC) Pointed at the person next to you\nD) Pointed towards you without a magazine cartridge","A)","This is correct as your handgun must always be pointed towards the range to ensure that an accident will not occur","This is incorrect as the only direction to point your handgun when operating it must be towards the range away from any personnel near the vicinity."),
    ("Handgun Familiarity & Safety", "It is possible to purchase a handgun at the age of 18.", "True/False", "True\nFalse", "False", "It is false which is correct as you must be 21 to legally purchase a handgun from a seller.", "You are incorrect as you must be 21 to legally purchase a handgun from a seller."),
    ("Handgun Familiarity & Safety", "A handgun will never misfire if the safety is used.","True/False","True\nFalse","False", "This statement is false as the safety doesn't prevent misfires from a handgun which is why it should always be unloaded at all times.","You are incorrect as the safety doesn't prevent misfires which could harm someone or cause an accident."),
    ("Handgun Familiarity & Safety", "Hiding a gun from the youth is a simple task at hand.","True/False","True\nFalse","False","This statement is false as handguns can be accessed by anyone if they are in sight or if they know how to access such firearm.","You are incorrect, it is not a simple task to hide a gun from the youth as they can always find a way to access your weapons."),
    ("Handgun Familiarity & Safety","A double-action revolver requires the hammer to be cocked and releasing it to fire.","True/False","True\nFalse","True", "This statement is True as the hammer actuates the revolver when released unlike other action revolvers.", "You chose incorrectly as the hammer must be cocked and released to actuate and fire a double-action revolver."),
    ("Handgun Familiarity & Safety", "What ammunition have we been shooting in class for demonstrations as it is the common ammunition for competitive handgun competitions?", "Short Answer", "", ".22", "Yes! .22 is commonly used by competitors for precision and accurate competitions along with in class.", "We use .22 ammunition. Thus, you are incorrect as .22 is also commonly used for competitions."),
    ("Handgun Familiarity & Safety","What action is the Glock we use in class for demonstrations?","Short Answer","","Strike-Fire","Yes it is a strike fire Glock as it implements the hammer to strike upon the striker on ammunition and doesn't require the hammer to be cocked","You are incorrect as it is a Strike-Fire Glock that can be shot without the hammer being cocked."),
    ("Handgun Familiarity & Safety","Where is the ammunition fed in a handgun?","Short Answer","","Chamber","The ammunition is fed into the chamber of the handgun as it is a part of the barrel.","This is incorrect as it is fed into the chamber of the handgun as it is a part of the barrel."),
    # Category 2
    ("American Literature", "Who wrote 'To Kill a Mockingbird'?", "MCQ", "A) Harper Lee\nB) John Steinbeck\nC) Mark Twain\nD) William Faulkner", "A)", "Yes, Harper Lee did write 'To Kill a Mockingbird'.", "Incorrect. The correct answer is Harper Lee as she is the true author of To Kill a Mockingbird."),
    ("American Literature", "Which novel features the character Holden Caulfield?", "MCQ", "A) The Great Gatsby\nB) The Catcher in the Rye\nC) Moby-Dick\nD) The Grapes of Wrath","B)","You are correct as Holden Caulfield appears in 'The Catcher in the Rye'.","You are Incorrect. The correct answer is The Catcher in the Rye."),
    ("American Literature", "Who wrote The Adventures of Huckleberry Finn?", "MCQ", "A) F. Scott Fitzgerald\nB) Ernest Hemingway\nC) Mark Twain\nD) John Steinbeck","C)","You are correct as 'The Adventures of Huckleberry Finn' was written by Mark Twain.","Incorrect, The correct answer is Mark Twain who also wrote The Prince and The Pauper and A Horse's Tale."),
    ("American Literature", "Which author wrote The Sound and the Fury?", "MCQ", "A) William Faulkner\nB) Toni Morrison\nC) Edith Wharton\nD) Virginia Woolf","A)","This is the correct choice as 'The Sound and the Fury' was written by William Faulkner.","You are incorrect as the correct answer is William Faulkner."),
    ("American Literature", "What is the title of the novel by F. Scott Fitzgerald that explores themes of decadence, idealism, and excess in Jazz Age America?", "MCQ", "A) The Great Gatsby\nB) Tender Is the Night\nC) This Side of Paradise\nD) The Beautiful and Damned","A)","This is correct as The Great Gatsby truly explores themes of decadence, idealism, and excess in Jazz Age America.","You are incorrect. The correct answer is The Great Gatsby as it best explores these themes."),
    ("American Literature", "Who wrote the novel 'Invisible Man', published in 1952?", "Short Answer", "", "Ralph Ellison","Correct! Ralph Ellison is the author of Invisible Man", "Incorrect. The correct answer is Ralph Ellison."),
    ("American Literature", "What is the title of Ernest Hemingway's famous novel published in 1926?", "Short Answer", "", "The Sun Also Rises","This is correct!, The Sun Also Rises was published in 1926.","That's incorrect. The correct answer is The Sun Also Rises."),
    ("American Literature", "Who is the author of 'The Grapes of Wrath'?", "Short Answer", "", "John Steinbeck","You are correct as John Steinbeck is the author of Grapes of Wrath read in class.","Wrong. The correct answer is John Steinbeck."),
    ("American Literature", "It is possible for authors to write under pen names.", "True/False", "True\nFalse", "True", "You are correct as Authors can indeed write under pen names.", "Incorrect. The statement is true and that authors can write under pen names."),
    ("American Literature", "Shakespeare is known for his contributions to American Literature.", "True/False", "True\nFalse", "False", "You are correct! Shakespeare is not known for his contributions to American Literature.", "Incorrect. The statement is false as he is not known for his contributions to American Literature."),
    # Category 3
    ("Database Management", "What does SQL stand for?", "MCQ", "A) Structured Query Language\nB) Simple Query Language\nC) Static Query Language\nD) Standardized Query Language", "A)", "Yes this is correct as SQL stands for Structured Query Language.", "Incorrect. The correct answer is Structured Query Language."),
    ("Database Management", "Which command is used to retrieve data from a database?", "MCQ", "A) UPDATE\nB) INSERT\nC) SELECT\nD) DELETE","C)","You are right! SELECT is used to retrieve data from a database.","Incorrect. The correct answer is SELECT."),
    ("Database Management", "What does the acronym ACID stand for in the context of database transactions?", "MCQ", "A) Atomicity, Consistency, Isolation, Durability\nB) Association, Commitment, Integrity, Durability\nC) Atomicity, Consistency, Integrity, Durability\nD) Association, Consistency, Isolation, Durability","A)","The term ACID stands for Atomicity, Consistency, Isolation, Durability in the context of database transactions.","Incorrect. The correct answer is Atomicity, Consistency, Isolation, Durability."),
    ("Database Management", "What is a primary key in a relational database?", "MCQ", "A) A unique identifier for a row in a table\nB) A foreign key that links two tables\nC) An index for fast data retrieval\nD) A constraint that enforces data integrity","A)","A primary key is a unique identifier for a row in a table, You are Correct.","Incorrect. The correct answer is A unique identifier for a row in a table."),
    ("Database Management", "Which type of database model organizes data into tables?", "MCQ", "A) Hierarchical\nB) Relational\nC) Network\nD) Object-Oriented","B)","You are correct as relational databases organize data into tables.","Incorrect. The correct answer is Relational."),
    ("Database Management", "What is the purpose of the SQL DELETE statement?", "Short Answer", "", "To delete records from a table","You are correct as it is used to delete records from a table.", "You are Wrong. The correct answer is To delete records from a table."),
    ("Database Management", "What is the purpose of a foreign key in a relational database?", "Short Answer", "", "To link tables together","This is correct as it links tables together.", "This is incorrect. The correct answer is To link tables together."),
    ("Database Management", "Define normalization in the context of database design.", "Short Answer", "", "Process of organizing data to minimize redundancy","You are correct, it organizes data to minimize redudancy as we trade efficiency for effectiveness.", "That's incorrect. The correct answer is Process of organizing data to minimize redundancy."),
    ("Database Management", "A database administrator manages data but does not deal with database security.", "True/False", "True\nFalse", "False", "You are Correct! A database administrator also deals with database security.", "Incorrect. A database administrator deals with the security of a database."),
    ("Database Management", "In a relational database, each table can have only one primary key.", "True/False", "True\nFalse", "True", "Correct! Each table in a relational database can have only one primary key.", "Incorrect. Each table can only have one primary key."),
    # Category 4
    ("Programming Logic & Analytic Thinking", "What is the output of 3 + 5 * 2?", "MCQ", "A) 16\nB) 13\nC) 11\nD) 10", "B)", "You are Correct, 3 + 5 * 2 does equal 13.", "Incorrect. The correct answer is 13."),
    ("Programming Logic & Analytic Thinking", "What is the result of the expression 10 % 3?", "MCQ", "A) 0\nB) 1\nC) 2\nD) 3", "B)", "You are Correct, 10 % 3 simply equals 1.", "Incorrect. The correct answer is 1."),
    ("Programming Logic & Analytic Thinking", "What is the value of the expression (4 > 2) and (3 < 5)?", "MCQ", "A) True\nB) False", "A)", "Yes, you are correct as (4 > 2) and (3 < 5) evaluates to True.", "Incorrect. The correct answer is True and not False in this scenario."),
    ("Programming Logic & Analytic Thinking", "What does the 'not' operator do in Python?", "MCQ", "A) Reverses the logical state of its operand\nB) Compares two values\nC) Raises a number to a power\nD) Checks if a value exists in a sequence","A)","This is correct, The 'not' operator reverses the logical state of its operand.","Incorrect. The correct answer is Reverses the logical state of its operand."),
    ("Programming Logic & Analytic Thinking", "What is the purpose of loops in programming?", "MCQ", "A) To repeat a block of code multiple times\nB) To execute code only if a condition is true\nC) To define a function\nD) To declare variables","A)","Yes, Loops are used to repeat a block of code multiple times. Thus, You are correct.","Incorrect. The correct answer is To repeat a block of code multiple times."),
    ("Programming Logic & Analytic Thinking", "What is the output of the following Python code?\nprint(2 ** 3)", "Short Answer", "", "8","You are correct as it prints 8","Incorrect. The correct output is 8."),
    ("Programming Logic & Analytic Thinking", "Explain what a Boolean variable is.", "Short Answer", "", "A variable that can have one of two values: True or False","This is correct as a variable can have one of two values: True or False.","That's incorrect. The correct answer is a variable that can have one of two values: True or False."),
    ("Programming Logic & Analytic Thinking", "What is a conditional statement in programming?", "Short Answer", "", "A statement that performs different actions depending on whether a condition is true or false","Correct! a conditional statement performs different actions depnding on whether a condition is true or false.", "Wrong. The correct answer is a statement that performs different actions depending on whether a condition is true or false."),
    ("Programming Logic & Analytic Thinking", "Python is a compiled language.", "True/False", "True\nFalse", "False", "You are Correct! Python is an interpreted language.", "Incorrect. The statement is false."),
    ("Programming Logic & Analytic Thinking", "A 'for' loop in Python is used to execute a block of code only if a condition is true.", "True/False", "True\nFalse", "False", "Correct! A 'for' loop in Python is used to iterate over a sequence of items.", "Incorrect. The statement is false as it is used to iterate over a sequence of items."),
    # Category 5
    ("Topics in British Literature", "Who wrote 'Pride and Prejudice'?", "MCQ", "A) Charles Dickens\nB) Jane Austen\nC) William Shakespeare\nD) Emily Brontë", "B)", "You are Correct! 'Pride and Prejudice' was written by Jane Austen.", "Incorrect. The correct answer is Jane Austen."),
    ("Topics in British Literature", "Which Shakespeare play features the character Hamlet?", "MCQ", "A) Romeo and Juliet\nB) Macbeth\nC) Hamlet\nD) Othello","C)","yes, ironically Hamlet is featured in the play 'Hamlet'.","Incorrect. The correct answer is Hamlet as he is featured in his own self-titled play."),
    ("Topics in British Literature", "Who wrote the poem 'Paradise Lost'?", "MCQ", "A) John Milton\nB) Geoffrey Chaucer\nC) William Wordsworth\nD) Samuel Taylor Coleridge","A)","You are Correct! 'Paradise Lost' was written by John Milton.","Incorrect. The correct author is John Milton."),
    ("Topics in British Literature", "What is the title of Emily Brontë's only novel?", "MCQ", "A) Wuthering Heights\nB) Jane Eyre\nC) Middlemarch\nD) Sense and Sensibility","A)","You are right as Emily Brontë's only novel is 'Wuthering Heights'.","Incorrect. The correct novel is Wuthering Heights."),
    ("Topics in British Literature", "Who is the author of 'Oliver Twist'?", "MCQ", "A) Charles Dickens\nB) Charlotte Brontë\nC) Daphne du Maurier\nD) George Eliot","A)","You chose correctly as 'Oliver Twist' was written by Charles Dickens.","Incorrect. The correct author is Charles Dickens."),
    ("Topics in British Literature", "What is the title of William Wordsworth's autobiographical poem?", "Short Answer", "", "The Prelude","You are correct as it is titled 'The Prelude'","That's incorrect. The correct answer is The Prelude."),
    ("Topics in British Literature", "Who wrote the poem 'The Waste Land'?", "Short Answer", "", "T.S. Eliot","You are Right! T.S. Eliot is the author of 'The Waste Land'","Wrong. The correct answer is T.S. Eliot."),
    ("Topics in British Literature", "What is the title of George Orwell's dystopian novel published in 1949?", "Short Answer", "", "1984","You are correct, it is titled 1984, yet published in 1949 ","Incorrect. The correct answer is 1984."),
    ("Topics in British Literature", "Mary Shelley is the author of 'Frankenstein'.", "True/False", "True\nFalse", "True", "Mary Shelley is indeed the author of 'Frankenstein'.", "Incorrect. The statement is true as she is the author of 'Frankenstein'."),
    ("Topics in British Literature", "Shakespeare's play 'Romeo and Juliet' is a tragedy.", "True/False", "True\nFalse", "True", "Correct! 'Romeo and Juliet' is classified as a tragedy.", "Incorrect. The statement is true as it is classified as a tragedy by credible critics.")
]

# Instance Creation
quiz_db = QuizDatabase()

# Table Creation
quiz_db.create_table()

# Insertion of sample data into the database
quiz_db.insert_questions(questions_data)

quiz_db.close_connection()
