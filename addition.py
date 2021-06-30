import datetime
from product import Product
import time
def validate(string):
    try:
        datetime.datetime.strptime(string, '%Y-%m-%d')
    except:
        return False
    return True
def addition():
    print('welcome to Addition')
    select = int(input('Which item you want to add 1 for book, 2 for series, 3 for movie :  '))
    if select == 1:
        type = 'book'
        status=True
    elif select == 2:
        type = 'series'
        status=True
    elif select == 3:
        type = 'movie'
        status=True
    else:
        print('Type is invalid input type correctly')
        time.sleep(1)
        cmd=input('Do you want to abort the operation if yes type yes')
        if cmd.lower()=='yes':
            return 0
        else:
            pass

    name = str(input('Enter the name: '))
    while(True):
        temp_date = str(input('Enter starting date(yyyy/mm/dd):  '))
        if temp_date == '':
            start_date = ''
            break
        else:
            if validate(temp_date):
                start_date = temp_date
                break
            else:
                print('Date is in incorrect format type again')
                time.sleep(1)
                cmd=input('Do you want to abort the operation if yes type yes')
                if cmd.lower()=='yes':
                    return 0
                else:
                    pass
     #Loop for starting date
    while(True):
        temp_date = str(input('Enter Ending date(yyyy/mm/dd):  '))
        if temp_date == '':
            end_date = ''
            break
        else:
            if validate(temp_date):
                end_date = temp_date
                status=False
                break
            else:
                print('End date is in incorrect format type again')
                cmd=input('Do you want to abort the operation if yes type yes')
                if cmd.lower()=='yes':
                    return 0
                else:
                    pass
    while(True):
        temp_con_time=input('Enter consumption time(in hours): ')
        if temp_con_time=='':
            consump_time=0
            break
        elif temp_con_time.replace('.','1').isdigit():
            consump_time=float(temp_con_time)
            break
        else:
            print('Please input consumption hours in numbers correctly')
            time.sleep(1)
            cmd=input('Do you want to abort the operation if yes type yes')
            if cmd.lower()=='yes':
                return 0
            else:
                pass
    while(True):
        temp_rating=input('Enter personal ratings(0-10): ')
        if temp_rating=='':
            rating=0
            break
        elif temp_rating.replace('.','').isdigit():
            if float(temp_rating)<=10:
                rating=float(temp_rating)
                break
            else:
                rating=10.
                break
        else:
            print('Please rating in numbers correctly')
            time.sleep(1)
            cmd=input('Do you want to abort the operation if yes type yes')
            if cmd.lower()=='yes':
                return 0
            else:
                pass
                
    while(True):
        temp_tot_consump_day=input('Enter total consumption days: ')
        if temp_tot_consump_day=='':
            tot_consump_day=0
            break
        elif temp_tot_consump_day.isdigit():
            tot_consump_day=int(temp_tot_consump_day)
            break
        else:
            print('Please days in numbers correctly')
            time.sleep(1)
            cmd=input('Do you want to abort the operation if yes type yes')
            if cmd.lower()=='yes':
                return 0
            else:
                pass
    p=Product(name,start_date,end_date,consump_time,rating,tot_consump_day,type,status)
    return p