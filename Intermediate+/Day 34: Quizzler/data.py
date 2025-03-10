import requests
questionnaire=requests.get('https://opentdb.com/api.php?amount=10&type=boolean')
question_data=questionnaire.json()['results']
