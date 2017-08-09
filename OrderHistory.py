from Order import *

# Read previous orders from logfile and save it's contents to a list of Orders.
# First line contains the log of served foods

class OrderHistory:
    def __init__(self):
        # Open logfile
        self.logfile = 'KAS-log.txt'
        with open(self.logfile, 'r+') as l:
            # Make a list of the lines of the logfile, without newlines
            logfile_lines = [line.rstrip('\n') for line in l]
            # Create the order history list
            self.order_history = []
            self.total_ordered = [0, 0, 0, 0]
            self.total_served = [0, 0, 0, 0]

            first_line = True
            for line in logfile_lines:
                if first_line:
                    # Total served
                    self.total_served = line.split(' ')
                    # Convert to ints
                    for i in range(4):
                        self.total_served[i] = int(self.total_served[i])
                    first_line = False
                else:
                    # Append old orders
                    self.order_history.append(Order(line))
            l.close()

        self.current_queue_number = self.order_history[-1].return_queue_number
        self.current_order = self.order_history[-1].return_ordered()



    def next_order(self):
        # If new order
        if self.current_queue_number == self.order_history[-1].return_queue_number:
            self.order_history.append(Order(str(self.current_queue_number + 1) + 8 * " 0"))
        else:
            self.current_queue_number += 1
            self.current_order = self.order_history[self.current_queue_number - 1].return_ordered()


    def previous_order(self):
        if self.current_queue_number > 1:
            self.current_queue_number -= 1
            self.current_order = self.order_history[self.current_queue_number - 1].return_ordered()


    def update_logfile(self):
        with open(self.logfile, 'w') as l:
            # Rewrite the whole logfile
            for order in self.order_history:
                line = str(order.return_queue_number())
                for o in order.return_ordered():
                    line += " " + str(o)
                l.write(line + '\n')
            l.close()


    def count_total_ordered(self):
        food_counts = [0, 0, 0, 0]
        for order in self.order_history:
            x = order.return_ordered
            for i in range(4):
                food_counts[i] += x[i]
        self.total_ordered = food_counts


    def update_total_served(self, new_serving):
        for i in range(4):
            self.total_served[i] += new_serving[i]


    def count_current_orders(self):
        current_orders = [0, 0, 0, 0]
        for i in range(4):
            current_orders[i] = self.total_ordered[i] - self.total_served[i]
        return current_orders


    def return_queue_number(self):
        return self.current_queue_number


    def new_order(self, order_string):
        self.current_order........... #TODO Orderin muuttaminen mapiksi


