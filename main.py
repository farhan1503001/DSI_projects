from product import Product
from addition import addition
from edition import edition, match_checker
import datetime
import time
import difflib
product_list = list()


if __name__ == '__main__':
    while(True):
        print('For addition input 1, for editing input 2, for display 3 ')
        cmd=int(input('Enter command : '))
        if cmd == 1:
            value=addition()
            if value==0:
                pass
            else:
                product_list.append(value)
        elif cmd==2:
            name,type=edition()
            for item in product_list:
                rt=match_checker(item,name,type)
                if rt==-1:
                    print('Sorry this consumable is not editable')
                    break
                elif rt=='matched':
                    changable=item
                    break
                else:
                    pass
            
        elif cmd==3:
            for item in product_list:
                print(item.get_name(),item.get_type(),item.get_start_date(),item.get_end_date(),item.get_tot_consump(),item.get_rating(),item.get_consump_day(),item.get_status())
        else:
            print('Operation Terminated.Breaking.....')
            time.sleep(3)