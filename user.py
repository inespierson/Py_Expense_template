from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    },
]

def add_user():
    # This function should create a new user, asking for its name
    user = prompt(user_questions)
    with open('users.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([user['name']])
    return