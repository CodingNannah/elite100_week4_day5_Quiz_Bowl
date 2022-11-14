import requests

url='https://cae-bootstore.herokuapp.com'

endpoint_login = '/login'
endpoint_user = '/user'

# Post
endpoint_my_questions = '/question'

# Put
endpoint_change_my_questions = '/question/<id>'

# Get
# These two require token:
endpoint_all_questions = '/question/all'
endpoint_my_questions = '/question'

# Delete
endpoint_delete_questions = '/question/<id>'


# Authentication - Registration                 # I should already be registered!
import json


def register_user(payload):
    payload_json_string = json.dumps(payload)
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(
        url + endpoint_user,
        data = payload_json_string,
        headers = headers
    )
    return response.text

dianas_payload={
        "email":"codingnannah@gmail.com",
        "first_name":"Diana",
        "last_name":"Barber",
        "password":"123"
}    

register_user(dianas_payload)
print(response.text)                    # why yellowed out?


# Authentication - Basic Auth
import base64

def login_user(user_name, password):
    
    auth_string = user_name +':'+password
    
    headers = {
        'Authorization': "Basic " + base64.b64encode(auth_string.encode()).decode()
    }

    user_data = requests.get(
        url + endpoint_login,
        headers = headers
    )
    return user_data.json()

print(login_user('codingnannah@gmail.com','123'))


# Authentication - Bearer Auth for PUT requests
    # requires token
diana = login_user('codingnannah@gmail.com','123')
print(diana['token'])

    # Edit user payload options

# import json

def edit_user(token, payload):
    payload_json_string = json.dumps(payload)
    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : 'Bearer ' + token
    }

    response = requests.put(
        url + endpoint_user,
        data = payload_json_string,
        headers = headers
    )
    return response.status_code

dianas_edit_payload = {
    "last_name": "Barber"
}
    

print(edit_user(diana['token'], dianas_edit_payload))

diana = login_user('codingnannah@gmail.com','123')
print(diana['last_name'])


# Post Requests
    # My questions

# Allows authenticated user (as author) to post questions and answers

# Post
endpoint_my_questions = '/question'

def my_questions(token, payload):                            # name of function + (authorization = token) (payload is q & A)
    payload_json_string = json.dumps(payload)
    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : 'Bearer ' + token
    }

    response = requests.put(
        url + endpoint_my_questions,
        data = payload_json_string,
        headers = headers
    )
    return response.status_code

"""example payload:
{
    "question":"What is bright orange with green on top and sounds like a parrot?",
    "answer":"parrot"
}

Add my questions -
    Multiple choice options allowed?
    Longer answers require the special case situation:
{
    "question":"What is made emptier by making it bigger?",
    "answer":"hole"
}

{
    "question":"Who is the tallest woman in the world?",
    "answer":"Statue of Liberty"
}

{
    "question":"Why did the fox cross the road?",
    "answer":"He was after the chicken"
}

{
    "question": What do you call a bundle of hay in a church?"
    "answer": Christian Bale."
}

{
    "question":"How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
    "answer":"Would that I knew!"
}

{
    "question":"What do you call a paper airplane that can't fly?",
    "answer":"stationery" (accept: stationary)
}

"""


# Put Requests
    # Change my question

# Edits a Question with the id <id> if the token owner is the author of the question

def edit_question(token, payload):                   # payload is dictionary with q &/or a
    payload_json_string = json.dumps(payload)
    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : 'Bearer ' + token
    }

    response = requests.put(
        url + endpoint_change_my_questions,
        data = payload_json_string,
        headers = headers
    )
    return response.status_code

"""  Request to /question/2
{
    "answer":"parrot"
}

# print(my_question['id'])
    Just change one of the options for:
{
    'question':'Why can you wear an upside-down canoe on your head?',
    'answer':'It's cap-sized'
}
    """


# GET Requests

# Gets all questions/answers that everyone submits

def get_all_questions():
    all_questions = requests.get(url+endpoint_all_questions)
    return all_questions.json()['all_questions']
all_questions = get_all_questions()

print(all_questions)

# Gets only authorized logged in user's questions/answers

def get_my_questions():
    my_questions = requests.get(url+endpoint_my_questions)
    return my_questions.json()['my_questions']
my_questions = get_my_questions()

print(my_questions)


# DELETE Requests:
    # User
def delete_user(token):
    
    headers = {
        'Authorization': "Bearer " + token
    }

    response = requests.delete(
        url + endpoint_user,
        headers = headers
    )
    return response.text

print(delete_user(jim['token']))

# check:
# jim = login_user('jimb@eam7.com','123')

    # My Questions
# Deletes a question with the id <id> if the token owner is the author of the question

def delete_questions(token):
    
    headers = {
        'Authorization': "Bearer " + token
    }

    response = requests.delete(
        url + endpoint_delete_questions,
        headers = headers
    )
    return response.text

print(delete_questions['id'])


# example DELETE endpoint to delete post with id 2: 
# DELETE https://cae-bootstore.herokuapp.com/question/2


# Make Application!
from getpass import getpass
import time                                     # why time? not used here
from IPython.display import clear_output
from IPython.display import Image
from IPython.display import display

def login(email):
    clear_output()
    password  =getpass("Password: ")
    user = login_user(email, password)
    return user

def register():
    clear_output()
    print("Registration:")
    email = input("Email: ")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    password = getpass("Password: ")
    
    user_dict = {
        "email":email,
        "first_name":first_name,
        "last_name":last_name,
        "password":password
    }
    return register_user(user_dict)


def main():
    pass
