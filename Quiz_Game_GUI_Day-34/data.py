import requests
NUM_QUESTIONS = 10
TYPE = 'boolean'

trivia_api = 'https://opentdb.com/api.php'

parameters = {
    'amount': NUM_QUESTIONS,
    'type': TYPE
}

response = requests.get(trivia_api,params = parameters)
response.raise_for_status()
data = response.json()
results = data['results']
question_data = results



