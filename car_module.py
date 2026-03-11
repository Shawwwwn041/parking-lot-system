#車牌辨識
def car_module(car_num):

    num_part = car_num.split("-") 
    if len(num_part) == 2:
        return True
    else:
        return False