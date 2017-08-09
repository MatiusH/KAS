class Order:
    def __init__(self, logfile_line):
        # Create a list of logfile line contents
        logfile_line_list = logfile_line.split(' ')
        # Convert it to integers
        logfile_line_list = list(map(int, logfile_line_list))

        self.queue_number = logfile_line_list[0]
        self.ordered = [logfile_line_list[1], logfile_line_list[2], logfile_line_list[3], logfile_line_list[4]]


    def return_queue_number(self):
        return self.queue_number


    def return_ordered(self):
        return self.ordered


    def update_ordered(self, updated_orders):
        self.ordered = updated_orders




