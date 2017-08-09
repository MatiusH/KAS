from OrderHistory import *


class OrderHandling:
    def __init__(self):
        self.order_mode = True


    def run(self):
        try:
            while True:
                if self.order_mode:
                    command = input("New order = press ENTER, new serving = SPACE + ENTER ")
                    if command == "":
                        line = input("ORDER #" + str())