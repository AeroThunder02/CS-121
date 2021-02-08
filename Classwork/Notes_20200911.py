import math

todays_date = 20200911
print(todays_date)


def to_C(temp_F):
    '''
    Converts a temperature from Farenheit to Celcius
    0C = 32F
    Gap of 10C corresponds to 18F
    '''
    result = (temp_F - 32.)*(100./180.)
    return result

def to_F(temp_C):
    '''
    Converts a temperature from Celcius to Farenheit
    32F = 0C
    Gap of 18F corresponds to 10C
    '''
    result = (180./100.)*temp_C + 32.
    return result

def date_toString(num_date):
    '''
    Converts the numerical date of YYYYMMDD to text\

    Ex. 20200911 -> 'Sep 11 2020'
    '''

    #Break down number into YYYY, MM, DD
    year = num_date // 10000                    #YYYYMMDD -> YYYY
    month_day = num_date % 10000         #YYYYMMDD -> MMDD
    month = month_day // 100                   #MMDD -> MM
    day = month_day % 100                      #MMDD -> DD


    # map of MM 1 to Jan, MM 2 to Feb... MM 12 to Dec

    if month == 1:
        month_string = 'Jan.'
    elif month == 2:
        month_string = 'Feb.'
    elif month == 3:
        month_string = 'Mar.'
    elif month == 4:
        month_string = 'Apr.'
    elif month == 5:
        month_string = 'May.'
    elif month == 6:
        month_string = 'Jun.'
    elif month == 7:
        month_string = 'Jul.'
    elif month == 8:
        month_string = 'Aug.'
    elif month == 9:
        month_string = 'Sep.'
    elif month == 10:
        month_string = 'Oct.'
    elif month == 11:
        month_string = 'Nov.'
    elif month == 12:
        month_string = 'Dec.'
    else:
        # Default if something goes wrong
        month_string = 'XXX'
        return

    # to convert the numbers, we can use 'str' function
    return month_string + '  ' + str(day) + ', ' + str(year)
