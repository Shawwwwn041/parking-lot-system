#車牌辨識
def car_module(car_num):

    num_part = car_num.split("-") 
    if len(num_part) == 2:
        print(f"切開的結果為{num_part}") 
        return True
    else:
        print("車牌格式不正確！")
        return False