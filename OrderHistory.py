# Read previous orders from logfile and save it's contents to a list of Orders.
# First line contains the log of served foods

from Order import *


class OrderHistory:
    def __init__(self):
        # Open logfile
        self.logfile = 'KAS-log2'
        with open(self.logfile, 'r+') as l:
            # Make a list of the lines of the logfile, without newlines
            logfile_lines = [line.rstrip('\n') for line in l]
            # Create the order history list
            self.order_history = []
            self.total_ordered = [0, 0, 0, 0, 0, 0, 0, 0]
            self.total_served = [0, 0, 0, 0, 0, 0, 0, 0]

            # Append old orders
            for line in logfile_lines:
                buf_list = line.split(' ')
                # Make a list of the logfile line
                number = int(buf_list[0])
                food_num = int(buf_list[1])
                served = False
                if buf_list[2] == 'T':
                    served = True
                # Add new order to order history based on the logfile line
                self.order_history.append(Order(number, food_num, served))
            l.close()

        self.current_queue_number = self.order_history[-1].number
        self.current_order = self.order_history[-1]
        self.count_total_ordered()
        self.count_total_served()
        # print(self.order_history)



    def next_order(self):
        # If new order
        if self.current_queue_number == self.order_history[-1].number:
            self.current_queue_number += 1
            self.order_history.append(Order(self.current_queue_number, 0, False))
            self.current_order = self.order_history[self.current_queue_number]
        else:
            self.current_queue_number += 1
            self.current_order = self.order_history[self.current_queue_number]
        # print(self.order_history)
        self.count_total_ordered()


    def previous_order(self):
        if self.current_queue_number > 1:
            self.current_queue_number -= 1
            self.current_order = self.order_history[self.current_queue_number]


    def update_logfile(self):
        with open(self.logfile, 'w') as l:
            # Rewrite the whole logfile
            # # First served foods
            # line = ""
            # for i in range(7):
            #     line += str(self.total_served[i]) + " "
            # line += str(self.total_served[7]) + '\n'
            # l.write(line)
            # Then all orders, including order numbers
            for order in self.order_history:
                served = "F"
                if order.served:
                    served = "T"
                line = str(order.number) + " " + str(order.food) + " " + served + '\n'
                # for j in range(8):
                #     line += " " + str(self.order_history[i][j])
                l.write(line)
            l.close()


    def count_total_ordered(self):
        food_counts = [0, 0, 0, 0, 0, 0, 0, 0]
        for order in self.order_history:
            if order.food > 0:
                food_counts[order.food - 1] += 1
        self.total_ordered = food_counts


    def count_total_served(self):
        food_counts = [0, 0, 0, 0, 0, 0, 0, 0]
        for order in self.order_history:
            if order.served:
                if order.food > 0:
                    food_counts[order.food - 1] += 1
        self.total_served = food_counts


    def submit_new_serving(self, new_serving):
        for i in range(8):
            self.total_served[i] += int(new_serving[i])


    def count_current_orders(self):
        current_orders = [0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(8):
            current_orders[i] = self.total_ordered[i] - int(self.total_served[i])
        return current_orders


    def count_current_orders_str(self):
        current_orders_str = ""
        for i in range(8):
            current_orders_str += " " + str(self.total_ordered[i] - int(self.total_served[i]))
        return current_orders_str


    def return_queue_number(self):
        return self.current_queue_number


    def return_current_order_str(self):
        string = ""
        for i in range(7):
            string += str(self.current_order[i]) + " "
        string += str(self.current_order[7])
        return string


    def return_order(self, num):
        return self.order_history[num]


    # def food_1_up(self):
    #     self.current_order = 1
    #
    # def food_2_up(self):
    #     self.current_order = 2
    #
    # def food_3_up(self):
    #     self.current_order = 2
    #
    # def food_4_up(self):
    #     self.current_order[3] += 1
    #
    # def food_5_up(self):
    #     self.current_order[4] += 1
    #
    # def food_6_up(self):
    #     self.current_order[5] += 1
    #
    # def food_7_up(self):
    #     self.current_order[6] += 1
    #
    # def food_8_up(self):
    #     self.current_order[7] += 1
    #
    #
    # def food_1_down(self):
    #     if self.current_order[0] > 0:
    #         self.current_order[0] -= 1
    #
    # def food_2_down(self):
    #     if self.current_order[1] > 0:
    #         self.current_order[1] -= 1
    #
    # def food_3_down(self):
    #     if self.current_order[2] > 0:
    #         self.current_order[2] -= 1
    #
    # def food_4_down(self):
    #     if self.current_order[3] > 0:
    #         self.current_order[3] -= 1
    #
    # def food_5_down(self):
    #     if self.current_order[4] > 0:
    #         self.current_order[4] -= 1
    #
    # def food_6_down(self):
    #     if self.current_order[5] > 0:
    #         self.current_order[5] -= 1
    #
    # def food_7_down(self):
    #     if self.current_order[6] > 0:
    #         self.current_order[6] -= 1
    #
    # def food_8_down(self):
    #     if self.current_order[7] > 0:
    #         self.current_order[7] -= 1
    #
    #
    #
    #
