from PyInquirer import prompt
import csv

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"input",
        "name":"other users involved",
        "message":"New Expense - Other users involved: ",
    },

]

def get_users():
    users = []
    with open('users.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            users.append(row[0])
    return users

def choose_user():
    users = get_users()
    user_questions = [
        {
            "type":"list",
            "name":"name",
            "message":"New Expense - Spender: ",
            "choices": users
        },
    ]
    user = prompt(user_questions)
    return user['name']


def new_expense(*args):
    infos = prompt(expense_questions)
    infos['spender'] = choose_user()
    print("Expense Added !")
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with open('expense_report.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([infos['amount'], infos['label'], infos['spender'], infos["other users involved"]])
    return True


