class Product:
    def __init__(self,name,start_date,end_date,tot_consump,rating,tot_day_consump,type,status=True):
        self.__name=name
        self.__start_date=start_date
        self.__end_date=end_date
        self.__tot_consump=tot_consump
        self.__rating=rating
        self.__tot_day_consump=tot_day_consump
        self.__type=type
        self.__editable=status
    def get_name(self):
        return self.__name
    def set_name(self,value):
        self.__name=value
    def get_start_date(self):
        return self.__start_date
    def set_start_date(self,value):
        self.__start_date=value
    def get_end_date(self):
        return self.__end_date
    def set_name(self,value):
        self.__end_date=value
    def get_tot_consump(self):
        return self.__tot_consump
    def set_tot_consump(self,value):
        self.__tot_consump=value
    def get_rating(self):
        return self.__rating
    def set_rating(self,value):
        self.__rating=value
    def get_consump_day(self):
        return self.__tot_day_consump
    def set_consump_day(self,value):
        self.__tot_day_consump=value
    def get_status(self):
        return self.__editable
    def set_status(self,value=True):
        self.__editable=value
    def get_type(self):
        return self.__type
        
