from display import display_view
from deletion import deletion
from product import Product
from addition import addition
from edition import change_add_date, edition, match_checker, update_consume_time,update_rating
import datetime
import time
import difflib
product_list = list()


if __name__ == '__main__':
    while(True):
        print('For addition input 1, for editing input 2, for display 3 ')
        cmd=input('Enter command : ')
        if cmd.isdigit():
            cmd=int(cmd)
        else:
            break
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
                    if input('Change consumptime(hours)? if yes press y else anything :')=='y':
                        ch_time=update_consume_time(item)
                        if ch_time is None:
                            continue
                        if input('Add consumption day? if yes press y else anything:  ')=='y':
                            ch_day=item.get_consump_day()+1
                            if ch_day is None:
                                pass
                            else:
                                item.set_consump_day(ch_day)
                        else:
                            item.set_tot_consump(ch_time)
                    else:
                        pass
                    if input('Change the ratings? if yes press y else anything:  ')=='y':
                        ch_rating=update_rating(item)
                        if ch_rating is None:
                            pass
                        else:
                            item.set_rating(ch_rating)
                    else:
                        pass

                    if input('Add consumption end date? if yes press y else anything: ')=='y':
                        ch_end_date_status=change_add_date(item)
                        if ch_end_date_status is None:
                            pass
                        else:
                            item.set_end_date(ch_end_date_status)
                            item.set_status(False)
                    else:
                        pass
                    break

                else:
                    pass
        elif cmd==3:
            name,type=deletion()
            for item in product_list:
                result=match_checker(item,name,type)
                if result=='matched':
                    if input('Do you want to delete it? if yes press y :')=='y':
                        item.set_name=''
                        item.set_start_date=''
                        item.set_end_date=''
                        item.set_rating=''
                    
                    else:
                        pass
            
        elif cmd==4:
            display_view(product_list)
            '''
            for item in product_list:
                print(item.get_name(),item.get_type(),item.get_start_date(),item.get_end_date(),item.get_tot_consump(),item.get_rating(),item.get_consump_day(),item.get_status())
            '''
        else:
            print('Operation Terminated.Breaking.....')
            time.sleep(3)