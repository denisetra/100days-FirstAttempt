import pandas as pd

## CREATE a csv that is called squirrel_count that contains fur color.
## How many grey squirrels are there, how many cinnimons, how many grey.
## Create new dataframe with the data, create a final CSV (color, & number)
in_file = '2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'
data = pd.read_csv(in_file)

gray_fur = len(data[data["Primary_Fur_Color"] == 'Gray'])
cinnamon_fur = len(data[data["Primary_Fur_Color"] == 'Cinnamon'])
black_fur = len(data[data["Primary_Fur_Color"] == 'Black'])

fur_dict = {
    'Fur_Color' : ['Gray', 'Cinnamon', 'Black'],
    'Count' : [gray_fur, cinnamon_fur, black_fur]
}

my_data = pd.DataFrame(fur_dict)
my_data.to_csv('2018-Squirrel-Count-by-Fur_Color.csv')








