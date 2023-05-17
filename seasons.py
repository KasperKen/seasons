input_month = input()
input_day = int(input())

seasons = [{
    'name': 'Spring',
    'months': {
        'March': {'from': 20, 'to': 31},
        'April': {'from': 1, 'to': 30},
        'June': {'from': 1, 'to': 20 }
    }
},
{
    'name': 'Summer',
    'months': {
        'June': {'from': 21, 'to': 30},
        'July': {'from': 1, 'to': 31},
        'August': {'from': 1, 'to': 31},
        'September': {'from': 1, 'to': 21}
    }
},
{
    'name': 'Autumn',
    'months': {
        'September': {'from': 22, 'to': 30},
        'October': {'from': 1, 'to': 31},
        'November': {'from': 1, 'to': 30},
        'December': {'from': 1, 'to': 20}
    }
},
{
    'name': 'Winter',
    'months': {
        'December': {'from': 21, 'to': 31},
        'January': {'from': 1, 'to': 31},
        'Februrary': {'from': 1, 'to': 29},
        'March': {'from': 1, 'to': 19}
    }
}]


def check_season(month, day):
    for season in seasons:
        if month in season['months'] and season['months'][month]['from'] <= day <= season['months'][month]['to']:
            return season['name']
    return 'Invalid'


print(check_season(input_month, input_day))
