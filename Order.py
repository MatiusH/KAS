class Order:
    def __init__(self, logfile_line):
        # Create a list of logfile line contents
        logfile_line_list = logfile_line.split(' ')
        # Convert it to integers
        logfile_line_list = list(map(int, logfile_line_list))

        self.queue_number = logfile_line_list[0]
        self.ordered = [logfile_line_list[1], logfile_line_list[2], logfile_line_list[3], logfile_line_list[4]]
        self.served = [logfile_line_list[5], logfile_line_list[6], logfile_line_list[7], logfile_line_list[8]]


    def return_queue_number(self):
        return self.queue_number


    def return_ordered(self):
        return self.ordered


    def return_served(self):
        return self.served


    def update_ordered(self, updated_orders):
        self.ordered = updated_orders


    def update_served(self, updated_served):
        self.served = updated_served


