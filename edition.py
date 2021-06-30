import time
from product import Product
import datetime
import difflib
def edition():
    print('welcome to edition part')
    print('........................')
    name=input('Enter the name of the product you want to edit: ')
    type=input('Enter the type of that product(1:book 2:series 3:movie): ')
    if type.lower=='book' or type.lstrip().rstrip()=='1':
        type='book'
    elif type.lower=='series' or type.lstrip().rstrip()=='2':
        type='series'
    elif type.lower=='movie' or type.lstrip().rstrip()=='3':
        type='movie'
    return name,type
def match_checker(item,name,type):
    if difflib.SequenceMatcher(None,item.get_name(),name).ratio()>=0.80:
        if item.get_type()==type:
            print('Product Name: '+item.get_name()+' Type: '+type+' Found')
            if item.get_status():
                return 'matched'
            else:
                return -1
#def update_consume_time(product):
