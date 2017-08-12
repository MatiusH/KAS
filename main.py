from OrderHistory import *


def main():
    oh = OrderHistory()
    order_mode = True

    try:
        while True:
            if order_mode:
                print("ORDER #" + str(oh.return_queue_number()) + ": " + oh.return_current_order_str())
                command = input("Next order = 'n', previous order = 'p', serve = 'RETURN':")
                # Next order
                if command == 'n':
                    oh.next_order()
                # Previous order
                elif command == 'p':
                    oh.previous_order()

                # Serving
                elif command == "":
                    line = input("Input foods :")
                    oh.update_total_served(line)
                    print(oh.count_current_orders())


    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
