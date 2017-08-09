from OrderHistory import *


def main():
    oh = OrderHistory()
    order_mode = True

    try:
        while True:
            if self.order_mode:
                command = input(
                    "New order = press ENTER, new serving = SPACE + ENTER ")
                if command == "":
                    line = input("ORDER #" + str(oh.return_queue_number()) + " : food1 food2 food3 food4 ")
                    #TODO tilaaminen


    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
