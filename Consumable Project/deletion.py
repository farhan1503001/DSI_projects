import time
from product import Product
from edition import validate
import difflib
def deletion():
    print('welcome to edition part')
    print('........................')
    name = input('Enter the name of the product you want to delete: ')
    type = input('Enter the type of that product(1:book 2:series 3:movie): ')
    if type.lower == 'book' or type.lstrip().rstrip() == '1':
        type = 'book'
    elif type.lower == 'series' or type.lstrip().rstrip() == '2':
        type = 'series'
    elif type.lower == 'movie' or type.lstrip().rstrip() == '3':
        type = 'movie'
    return name, type
def del_match_checker(item,name,type):
    if difflib.SequenceMatcher(None, item.get_name(), name).ratio() >= 0.80:
        if item.get_type() == type:
            print('Product Name: '+item.get_name()+' Type: '+type+' Found')
            return 'matched'
    else:
        pass