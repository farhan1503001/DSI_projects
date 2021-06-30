import sqlite3
from sqlite3.dbapi2 import connect
from display import display_view,oneview
from deletion import deletion,del_match_checker
from product import Product
from addition import addition
from edition import change_add_date, edition, match_checker, update_consume_time,update_rating
import datetime
import time
import difflib
product_list = list()
connection=sqlite3.connect('consumable.sqlite3')
curr=connection.cursor()
temp_list=curr.execute('select * from product').fetchall()
if len(temp_list)>0:
    for item in temp_list:
        p=Product(item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8])
        product_list.append(p)
if __name__ == '__main__':
    while(True):
        print('For addition input 1, for editing input 2, 3 for deleting entry, 4 for display,5 for overview ')
        cmd=input('Enter command : ')
        if cmd.isdigit():
            cmd=int(cmd)
        else:
            print('Input DIGITS correctly please!')
        if cmd == 1:
            value=addition()
            if value==0:
                pass
            else:
                curr.execute('insert into product(name,type,start_date,end_date,total_consumption,total_rating,total_day_consumption,status) values(?,?,?,?,?,?,?,?)',
                (value.get_name(),value.get_type(),value.get_start_date(),value.get_end_date(),
                value.get_tot_consump(),value.get_rating(),value.get_consump_day(),value.get_status()))
                connection.commit()
                product_list.append(value)
        elif cmd==2:
            name,type=edition()
            count=1
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
                                item.set_tot_consump(ch_time)
                                curr.execute('update product set total_day_consumption=?,total_consumption=? where id=?',(ch_day,ch_time,count))
                                connection.commit()
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
                            curr.execute('update product set total_rating=? where id=?',(ch_rating,count))
                            connection.commit()
                    else:
                        pass

                    if input('Add consumption end date? if yes press y else anything: ')=='y':
                        ch_end_date_status=change_add_date(item)
                        if ch_end_date_status is None:
                            pass
                        else:
                            item.set_end_date(ch_end_date_status)
                            item.set_status(False)
                            curr.execute('update product set end_date=?,status=? where id=?',(ch_end_date_status,item.get_status(),count))
                            connection.commit()
                    else:
                        pass
                    break

                else:
                    count=count+1
        elif cmd==3:
            name,type=deletion()
            counter=1
            for item in product_list:
                result=del_match_checker(item,name,type)
                if result=='matched':
                    if input('Do you want to delete it? if yes press y :')=='y':
                        item.set_name('')
                        item.set_start_date('')
                        item.set_end_date('')
                        item.set_rating(0)
                        item.set_type('')
                        curr.execute('update product set name=?,type=?,start_date=?,end_date=?,total_rating=? where id=?',('','','','',0,counter))
                        connection.commit()
                    else:
                        pass
                else:
                    counter=counter+1
                        
            
        elif cmd==4:
            if input('Do you want to view elements by type? if yes press y: ')=='y':
              display_view(product_list)
            else:
                oneview(product_list)
            '''
            for item in product_list:
                print(item.get_name(),item.get_type(),item.get_start_date(),item.get_end_date(),item.get_tot_consump(),item.get_rating(),item.get_consump_day(),item.get_status())
            '''
        elif cmd==5:

        else:
            print('Operation Terminated.Breaking.....')
            time.sleep(3)
            