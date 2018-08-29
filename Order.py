# coding=utf-8

class Order:
    def __init__(self, number, food_num, served, food_name, o_time, s_time):
        self.number = number
        self.food = food_num
        self.served = served
        self.food_name = food_name
        self.order_time = o_time
        self.serving_time = s_time
