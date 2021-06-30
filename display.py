import time
from product import Product
import difflib
def display_view(product_list):
    while(True):
        print('For view press 1 for book,2 for series,3 for movie')
        type=input('Enter the type you want to see')
        if type.isdigit():
            if int(type)==1:
                section='book'
                for item in product_list:
                    if item.get_type()==section:
                        print(item.get_name(),item.get_type(),item.get_start_date(),item.get_end_date(),
                        item.get_tot_consump(),item.get_rating(),item.get_consump_day(),item.get_status())
                        break
            elif int(type)==2:
                section='series'
                for item in product_list:
                    if item.get_type()==section:
                        print(item.get_name(),item.get_type(),item.get_start_date(),item.get_end_date(),
                        item.get_tot_consump(),item.get_rating(),item.get_consump_day(),item.get_status())
                        break
            elif int(type)==3:
                section='movie'
                for item in product_list:
                    if item.get_type()==section:
                        print(item.get_name(),item.get_type(),item.get_start_date(),item.get_end_date(),
                        item.get_tot_consump(),item.get_rating(),item.get_consump_day(),item.get_status())
                        
            else:
                print('Enter between 1,2,3')
        else:
            print('Follow the instructions to see')
            time.sleep(2)
            cmd=input('Do you want to abort the operation if yes type yes')
            if cmd.lower()=='yes':
                return
            else:
                pass
def oneview(product_list):
    name=input('Enter the name to search: ')
    flag=False
    for item in product_list:
        if difflib.SequenceMatcher(None,item.get_name(),name).ratio()>=0.86:
            print(item.get_name(),item.get_type(),item.get_start_date(),item.get_end_date(),
                item.get_tot_consump(),item.get_rating(),item.get_consump_day(),item.get_status())
            flag=True
            break
    if flag:
        return
    else:
        print('Not found')
        time.sleep(3)
        return
                


