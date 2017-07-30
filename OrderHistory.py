from Order import *


class OrderHistory:
    def __init__(self):
        # Open logfile
        self.logfile = 'KAS-log.txt'
        with open(self.logfile, 'r+') as l:
            # Make a list of the lines of the logfile, without newlines
            logfile_lines = [line.rstrip('\n') for line in l]
            # Create the order history list
            self.order_history = []
            for line in logfile_lines:
                self.order_history.append(Order(line))
            l.close()

        self.current_queue_number = self.order_history[-1].return_queue_number
        self.current_ordered = self.order_history[-1].return_ordered()
        self.current_served = self.order_history[-1].return_served()


    def next_order(self):
        # If new order
        if self.current_queue_number == self.order_history[-1].return_queue_number:
            self.order_history.append(Order(str(self.current_queue_number + 1) + 8 * " 0"))
        else:
            self.current_queue_number += 1
            self.current_ordered = self.order_history[self.current_queue_number - 1].return_ordered()
            self.current_served = self.order_history[self.current_queue_number - 1].return_served()


    def previous_order(self):
        if self.current_queue_number > 1:
            self.current_queue_number -= 1
            self.current_ordered = self.order_history[self.current_queue_number - 1].return_ordered()
            self.current_served = self.order_history[self.current_queue_number - 1].return_served()


    def update_logfile(self):
        with open(self.logfile, 'w') as l:
            # Rewrite the whole logfile
            for order in self.order_history:
                line = str(order.return_queue_number())
                for o in order.return_ordered():
                    line += " " + str(o)
                for s in order.return_served():
                    line += " " + str(s)
                l.write(line + '\n')
            l.close()



