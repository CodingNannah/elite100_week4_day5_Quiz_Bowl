# Week 4 Project: Quiz Bowl!

Run the app (explain how!)
Follow prompts

## Instructions for Project Creation:
You Will Create a Quiz Creator/Taking App

Your App Will connect to https://cae-bootstore.herokuapp.com/
(Like We Did In class Yesterday)


There are new endpoints available.  See the Documentation on github to understand how they work:  https://github.com/CrtlAltElite/BookStoreAPI

Your Application should:
Login a user with Basic Auth
Allow Users to Register an account

If the user is anyone but you (doesn't has your google-classroom email address) then
You should create a quiz with 10 random questions from the API from all users questions [Note the API isn't starting with 10 questions]
After the question is completed you need to Award the user a score based on there correct or incorrect response

If the User is you (has your google-classroom email address) The user should be prompted with extra prompts that each work properly:
NOTE: They should also be able to take the quiz like a normal user
Create Question
Edit Question
Delete Question
View My Questions

As ALWAYS: add a README.md explaining your app and how to use it.

Make this as cool as you can!  If you want to make it harder try and make 'fuzzy' answers work (aka answer that should be right but don't match the answer string in the game perfectly)

### Map of Quiz Bowl Homework in Jupyter:

Authentication - Registration
Authentication - Basic
Authentication - Token

Post Requests
Put Requests
Get Requests
Delete Requests

Make an Application

### Endpoints
import requests

url='https://cae-bootstore.herokuapp.com'

endpoint_login = '/login'
endpoint_user = '/user'

Post:
endpoint_my_questions = '/question'

Put:
endpoint_change_my_questions = '/question/<id>'

Get:
* These two require token:
endpoint_all_questions = '/question/all'
endpoint_my_questions = '/question'

Delete:
endpoint_delete_questions = '/question/<id>'

