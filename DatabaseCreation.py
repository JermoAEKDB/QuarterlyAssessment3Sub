import sqlite3

# Database connection
conn = sqlite3.connect('quiz_questions.db')


c = conn.cursor()

#table creation for storing questions
c.execute('''CREATE TABLE IF NOT EXISTS questions (
             id INTEGER PRIMARY KEY,
             category TEXT,
             question TEXT,
             question_type TEXT,
             options TEXT,
             answer TEXT,
             feedback_correct TEXT,
             feedback_incorrect TEXT)''')

# Sample data of questions for each category
questions_data = [
    # Category 1
    ("Handgun Familiarity & Safety", "What is the heaviest grain of .22 ammunition?", "MCQ", "A) 55 Gr\nB) 60 Gr\nC) 30 Gr\nD) 40 Gr", "B", "Yes, you are correct as it is the heaviest weight", "This is incorrect as 60 Grain .22 ammo is the heaviest amongst the selections."),
    ("Handgun Familiarity & Safety", "What action for a handgun doesn't require the hammer or release to fire?", "MCQ", "A) Single-Action\nB) Double-Action\nC) Strike-Fire\nD) Single/double-Action","C","This is correct as a strike-fire handgun doesn't require the hammer or release to be used but a striker.","This is incorrect as the only action for a handgun that doesn't require a hammer or a release is the Strike-Fire action."),
    ("Handgun Familiarity & Safety","Where must a handgun always be pointed at the range?","MCQ","A) Towards the range\nB) Pointed down at your foot\nC) Pointed at the person next to you\nD) Pointed towards you without a magazine cartridge","A","This is correct as your handgun must always be pointed towards the range to ensure that an accident will not occur","This is incorrect as the only direction to point your handgun when operating it must be towards the range away from any personnel near the vicinity."),
    ("Handgun Familiarity & Safety", "It is possible to purchase a handgun at the age of 18.", "True/False", "", "False", "It is false which is correct as you must be 21 to legally purchase a handgun from a seller.", "You are incorrect as you must be 21 to legally purchase a handgun from a seller."),
    ("Handgun Familiarity & Safety", "A handgun will never misfire if the safety is used.","True/False","","False", "This statement is false as the safety doesn't prevent misfires from a handgun which is why it should always be unloaded at all times.","You are incorrect as the safety doesn't prevent misfires which could harm someone or cause an accident."),
    ("Handgun Familiarity & Safety", "Hiding a gun from the youth is a simple task at hand.","True/False","","False","This statement is false as handguns can be accessed by anyone if they are in sight or if they know how to access such firearm.","You are incorrect, it is not a simple task to hide a gun from the youth as they can always find a way to access your weapons."),
    ("Handgun Familiarity & Safety","A double-action revolver requires the hammer to be cocked and releasing it to fire.","True/False","","True", "This statement is True as the hammer actuates the revolver when released unlike other action revolvers.", "You chose incorrectly as the hammer must be cocked and released to actuate and fire a double-action revolver."),
    ("Handgun Familiarity & Safety", "What ammunition have we been shooting in class for demonstrations as it is the common ammunition for competitive handgun competitions?", "Short Answer", "", ".22", "Yes! .22 is commonly used by competitors for precision and accurate competitions along with in class.", "We use .22 ammunition. Thus, you are incorrect as .22 is also commonly used for competitions."),
    ("Handgun Familiarity & Safety","What action is the Glock we use in class for demonstrations?","Short Answer","","Strike-Fire","Yes it is a strike fire Glock as it implements the hammer to strike upon the striker on ammunition and doesn't require the hammer to be cocked","You are incorrect as it is a Strike-Fire Glock that can be shot without the hammer being cocked."),
    ("Handgun Familiarity & Safety","Where is the ammunition fed in a handgun?","Short Answer","","Chamber","The ammunition is fed into the chamber of the handgun as it is a part of the barrel.","This is incorrect as it is fed into the chamber of the handgun as it is a part of the barrel."),
]

# Insert the sample data into the database
c.executemany('''INSERT INTO questions (category, question, question_type, options, answer, feedback_correct, feedback_incorrect)
                  VALUES (?, ?, ?, ?, ?, ?, ?)''', questions_data)

# Commit changes and close the connection
conn.commit()
conn.close()


