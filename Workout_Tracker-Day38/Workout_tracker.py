import requests, os
from datetime import datetime
activity_date = datetime.now().strftime('%Y%m%d')
activity_time = datetime.now().strftime('%H:%M')
#APP_ID = auth_keys_master.nutritionix_app_id
#APP_KEY = auth_keys_master.nutritionix_key
APP_ID = os.environ['APP_ID']
APP_KEY = os.environ['APP_KEY']
attribution = 'Data originates from Nutritionix.'
exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
GENDER = 'female'
HEIGHT_CM = '160'
WEIGHT_KG = '104.33'
AGE = '52'
###   Exercise Query  ###
headers = {'x-app-id': APP_ID,'x-app-key': APP_KEY,'x-remote-user-id': '0'}
my_exercise = input('Please enter the exercise that you performed. ')
exercise_check = {'query': my_exercise,'gender': GENDER,'weight_kg': WEIGHT_KG,'height_cm': HEIGHT_CM,'age': AGE}
my_response = requests.post(url=exercise_endpoint,json=exercise_check,headers=headers)
my_data = my_response.json()
### Sheety API for spreadsheet ###
basic_url = 'https://api.sheety.co/f6301e01d2bbf65409260452818ab619/deniseCodingGmailWorkoutTracker/workouts'
# object_id = ''  # Used with put & delete
# put_url = f'{basic_url}/{object_id}'
# delete_url = f'{basic_url}/{object_id}'
##sheety_auth = auth_keys_master.sheety_token
SHEETY_AUTH = os.environ['SHEETY_AUTH']
sheety_headers = {'Authorization': SHEETY_AUTH}

my_exercise_list = my_data['exercises']
for activity in my_exercise_list:
    activity_name = activity['name'].title()
    activity_calories = activity['nf_calories']
    activity_duration = activity['duration_min']
    my_workout = {'workout': {'date': activity_date,'time': activity_time,'exercise': activity_name,'duration': activity_duration,'calories': activity_calories}}
    print (my_workout)
    sky = requests.post(url=basic_url,json=my_workout, headers=sheety_headers)
    print (sky.text)