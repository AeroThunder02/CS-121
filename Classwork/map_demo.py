#
#map_demo
#

c_offset = 0
f_offset = 32

def to_C(temp_F):
    '''
    Converts a temperature from Farenheit to Celcius
    0C = 32F
    Gap of 10C corresponds to 18F
    '''
    return (100.0/180.0)*(temp_F-f_offset)+c_offset
    

def to_F(temp_C):
    '''
    Converts a temperature from Celcius to Farenheit
    32F = 0C
    Gap of 18F corresponds to 10C
    '''
    return (180.0/100.0)*(temp_C-c_offset) + f_offset
    

def temp_demo(f_list):

    #inner function
    def temp_threshold(c):
        return c > 37

    #first, map all temps to Celcius
    c_list = map(to_C, f_list)

    #filter out temperatures below 37
    threshold_list = filter(temp_threshold, c_list)

    return min(threshold_list)

def temp_demo_2(f_list):

    #inner function
    def temp_threshold(c):
        return c > 37

    #first, map all temps to Celcius
    c_list = map(to_C, f_list)

    #filter out temperatures below 37
    threshold_list = filter(temp_threshold, c_list)

    return len(list(threshold_list))

def temp_demo_3(f_list):

    #inner function
    def temp_threshold(c):
        return c > 37

    #first, map all temps to Celcius
    c_list = map(to_C, f_list)

    #filter out temperatures below 37
    threshold_list = list(filter(temp_threshold, c_list))

    return sum(threshold_list)/len(threshold_list)
