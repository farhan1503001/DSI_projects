import time
from product import Product
import sqlite3
import difflib
#Display based on product type
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
#Display based on product name
def oneview(product_list):
    name=input('Enter the name to search: ')
    flag=False
    for item in product_list:
        if difflib.SequenceMatcher(None,item.get_name(),name).ratio()>=0.86: #You don't have to enter name 100% accurately!
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

#Displaying overview
#choose to do it in rookie way
def overview(product_list):
    #Can be easily performed using sql query
    # tot_consump: select sum(total_consumption_days) from product where product.type!='' group by type
    #Consumption_hours
    tot_case=0
    book_case=0
    series_case=0
    movie_case=0
    for item in product_list:
        tot_case=tot_case+item.get_tot_consump()
        if item.get_type()=='book':
            book_case=book_case+item.get_tot_consump()
        elif item.get_type()=='series':
            book_case=book_case+item.get_tot_consump()
        elif item.get_type()=='movie':
            movie_case=movie_case+item.get_tot_consump()
    print('Total consumption hours','Book','series','movie')
    print('.................................................')
    print(tot_case,"  ",book_case,"  ",series_case,"  ",movie_case)
    print('\n')
    tot_case=0
    book_case=0
    series_case=0
    movie_case=0
    item=None
    for item in product_list:
        tot_case=tot_case+item.get_tot_consump()
        if item.get_type()=='book':
            book_case=book_case+item.get_consump_day()
        elif item.get_type()=='series':
            book_case=book_case+item.get_consump_day()
        elif item.get_type()=='movie':
            movie_case=movie_case+item.get_consump_day()
    print('Total consumption days','Book','series','movie')
    print('.................................................')
    print(tot_case,"  ",book_case,"  ",series_case,"  ",movie_case)
    print('\n')

    tot_case=0.
    book_case=0.0
    series_case=0.0
    movie_case=0.0
    item=None
    total=0
    book=0
    series=0
    movie=0
    for item in product_list:
        if item.get_type()!='':
            tot_case=tot_case+item.get_rating()
            total=total+1
        if item.get_type()=='book':
            book_case=book_case+item.get_rating()
            book=book+1
        elif item.get_type()=='series':
            book_case=book_case+item.get_rating()
            series=series+1
        elif item.get_type()=='movie':
            movie_case=movie_case+item.get_rating()
            movie=movie+1
    print('Average Rating','Book','series','movie')
    print('.................................................')
    print(tot_case/total,"   ",book_case/book,"   ",series_case/series,"   ",movie_case/movie)
    print('\n')
    print('No.Products','Books','serieses','movies')
    print('.................................................')
    print(total,"  ",book,"   ",series,"   ",movie)
    print('\n')

        

    

