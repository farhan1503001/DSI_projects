import time
from product import Product
from addition import validate
import datetime
import difflib


def edition():
    print('welcome to edition part')
    print('........................')
    name = input('Enter the name of the product you want to edit: ')
    type = input('Enter the type of that product(1:book 2:series 3:movie): ')
    if type.lower == 'book' or type.lstrip().rstrip() == '1':
        type = 'book'
    elif type.lower == 'series' or type.lstrip().rstrip() == '2':
        type = 'series'
    elif type.lower == 'movie' or type.lstrip().rstrip() == '3':
        type = 'movie'
    return name, type


def match_checker(item, name, type):
    if difflib.SequenceMatcher(None, item.get_name(), name).ratio() >= 0.80:
        if item.get_type() == type:
            print('Product Name: '+item.get_name()+' Type: '+type+' Found')
            if item.get_status():
                return 'matched'
            else:
                return -1


def update_consume_time(item):
    while(True):
        temp_con_time = input('Enter new consumption time(in hours): ')
        if temp_con_time == '':
            consump_time = 0
            break
        elif temp_con_time.replace('.', '1').isdigit():
            consump_time = float(temp_con_time)
            break
        else:
            print('Please input consumption hours in numbers correctly')
            time.sleep(1)
            cmd = input('Do you want to abort the operation if yes type yes')
            if cmd.lower() == 'yes':
                return 0
            else:
                pass
    return consump_time


def update_rating(item):
    while(True):
        temp_rating = input('Enter new personal ratings(0-10): ')
        if temp_rating.replace('.','').isdigit():
            if float(temp_rating)<=10:
                rating=float(temp_rating)
                return rating
            else:
                rating=10.
                return rating
        else:
            print('Please rating in numbers correctly')
            time.sleep(1)
            cmd=input('Do you want to abort the operation if yes type yes')
            if cmd.lower()=='yes':
                return None
            else:
                pass

def change_add_date(item):
     while(True):
        temp_date = str(input('Enter Ending date(yyyy-mm-dd):  '))
        if validate(temp_date) and (datetime.datetime.strptime(temp_date,'%Y-%m-%d')>=(datetime.datetime.strptime(item.get_start_date(),'%Y-%m-%d'))):
            end_date = temp_date
            return end_date
        else:
            print('End date is in incorrect format type again')
            print('Ending cannot be earlier than starting date!!!')
            cmd=input('Do you want to abort the operation if yes type yes')
            if cmd.lower()=='yes':
                return None
            else:
                pass


