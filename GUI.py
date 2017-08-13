from tkinter import *
from OrderHistory import *


class GUI(OrderHistory):
    def __init__(self):
        super().__init__()
        self.main_window = Tk()
        self.order_mode = True

        #################
        self.food_names = ["food1", "food2", "food3", "food4"]
        self.food_prices = [1.0, 2.0, 3.0, 4.0]

        self.new_serving = [0, 0, 0, 0]

        # Row 0
        self.button_order = Button(self.main_window, text="Order", background="green", state=DISABLED, command=self.order, width=6)
        self.button_serve = Button(self.main_window, text="Serve", background="grey", command=self.serve, width=6)
        self.label_queue_number_text = Label(self.main_window, text="Number:", width=8)
        self.label_queue_number = Label(self.main_window, text=str(self.return_queue_number()), width=8)
        self.label_spacer1 = Label(self.main_window, text=" ")
        self.label_ordered_foods = Label(self.main_window, text="Ordered foods:")
        self.label_ordered = Label(self.main_window, text=self.count_current_orders_str())
        self.button_order.grid(row=0, column=0)
        self.button_serve.grid(row=0, column=1)
        self.label_queue_number_text.grid(row=0, column=2)
        self.label_queue_number.grid(row=0, column=3)
        self.label_spacer1.grid(row=0, column=4)
        self.label_ordered_foods.grid(row=0, column=5)
        self.label_ordered.grid(row=0, column=6)
        # Row 1
        self.label_food_1_text = Label(self.main_window, text=self.food_names[0])
        self.label_food_2_text = Label(self.main_window, text=self.food_names[1])
        self.label_food_3_text = Label(self.main_window, text=self.food_names[2])
        self.label_food_4_text = Label(self.main_window, text=self.food_names[3])
        self.label_food_1_text.grid(row=1, column=0)
        self.label_food_2_text.grid(row=1, column=1)
        self.label_food_3_text.grid(row=1, column=2)
        self.label_food_4_text.grid(row=1, column=3)
        # Row 2
        food_counts = self.return_current_order_str().split(' ')
        self.label_food_1 = Label(self.main_window, text=food_counts[0])
        self.label_food_2 = Label(self.main_window, text=food_counts[1])
        self.label_food_3 = Label(self.main_window, text=food_counts[2])
        self.label_food_4 = Label(self.main_window, text=food_counts[3])
        self.label_total_text = Label(self.main_window, text="Total:")
        self.label_total = Label(self.main_window, text=(self.return_total_price_str()) + "€")
        self.label_food_1.grid(row=2, column=0)
        self.label_food_2.grid(row=2, column=1)
        self.label_food_3.grid(row=2, column=2)
        self.label_food_4.grid(row=2, column=3)
        self.label_total_text.grid(row=2, column=5)
        self.label_total.grid(row=2, column=6)
        # Row 3
        self.button_food_1_up = Button(self.main_window, text="↑", command=self.food_1_up_gui)
        self.button_food_2_up = Button(self.main_window, text="↑", command=self.food_2_up_gui)
        self.button_food_3_up = Button(self.main_window, text="↑", command=self.food_3_up_gui)
        self.button_food_4_up = Button(self.main_window, text="↑", command=self.food_4_up_gui)
        self.button_food_1_up.grid(row=3, column=0)
        self.button_food_2_up.grid(row=3, column=1)
        self.button_food_3_up.grid(row=3, column=2)
        self.button_food_4_up.grid(row=3, column=3)
        # Row 4
        self.button_food_1_down = Button(self.main_window, text="↓", command=self.food_1_down_gui)
        self.button_food_2_down = Button(self.main_window, text="↓", command=self.food_2_down_gui)
        self.button_food_3_down = Button(self.main_window, text="↓", command=self.food_3_down_gui)
        self.button_food_4_down = Button(self.main_window, text="↓", command=self.food_4_down_gui)
        self.button_submit = Button(self.main_window, text="Submit", state=DISABLED, command=self.submit_serving_gui, width=8)
        self.button_food_1_down.grid(row=4, column=0)
        self.button_food_2_down.grid(row=4, column=1)
        self.button_food_3_down.grid(row=4, column=2)
        self.button_food_4_down.grid(row=4, column=3)
        self.button_submit.grid(row=4, column=5)
        # Row 5
        self.label_food_1_price = Label(self.main_window, text=str(self.food_prices[0]) + "€")
        self.label_food_2_price = Label(self.main_window, text=str(self.food_prices[1]) + "€")
        self.label_food_3_price = Label(self.main_window, text=str(self.food_prices[2]) + "€")
        self.label_food_4_price = Label(self.main_window, text=str(self.food_prices[3]) + "€")
        self.button_previous = Button(self.main_window, text="Previous", command=self.previous, width=8)
        self.button_next = Button(self.main_window, text="Next", command=self.next, width=8)
        self.label_food_1_price.grid(row=5, column=0)
        self.label_food_2_price.grid(row=5, column=1)
        self.label_food_3_price.grid(row=5, column=2)
        self.label_food_4_price.grid(row=5, column=3)
        self.button_previous.grid(row=5, column=5)
        self.button_next.grid(row=5, column=6)

        self.main_window.mainloop()



    def order(self):
        self.button_order.configure(state=DISABLED, background="green")
        self.button_serve.configure(state=NORMAL, background="gray")
        self.toggle_mode()
        self.label_queue_number_text.configure(text="Number:")
        self.label_queue_number.configure(text=str(self.return_queue_number()))
        self.label_total_text.configure(text="Total:")
        self.label_total.configure(text=(self.return_total_price_str()) + "€")
        self.label_food_1_price.configure(text=str(self.food_prices[0]) + "€")
        self.label_food_2_price.configure(text=str(self.food_prices[1]) + "€")
        self.label_food_3_price.configure(text=str(self.food_prices[2]) + "€")
        self.label_food_4_price.configure(text=str(self.food_prices[3]) + "€")
        self.button_submit.configure(state=DISABLED)
        self.button_previous.configure(state=NORMAL)
        self.button_next.configure(state=NORMAL)


    def serve(self):
        self.button_order.configure(state=NORMAL, background="grey")
        self.button_serve.configure(state=DISABLED, background="red")
        self.toggle_mode()
        self.new_serving = [0, 0, 0, 0]
        self.update_food_count_labels()
        self.label_queue_number_text.configure(text="")
        self.label_queue_number.configure(text="")
        self.label_total_text.configure(text="")
        self.label_total.configure(text="")
        self.label_food_1_price.configure(text="")
        self.label_food_2_price.configure(text="")
        self.label_food_3_price.configure(text="")
        self.label_food_4_price.configure(text="")
        self.button_submit.configure(state=NORMAL)
        self.button_previous.configure(state=DISABLED)
        self.button_next.configure(state=DISABLED)






    def toggle_mode(self):
        self.order_mode ^= self.order_mode


    # Up- and down-button methods - gui-side ###########################################################################
    def food_1_up_gui(self):
        if self.order_mode:
            self.food_1_up()
            self.update_food_count_labels()
            self.label_total.configure(text=(self.return_total_price_str()) + "€")
        else:
            self.new_serving[0] += 1
            self.update_food_count_labels()


    def food_2_up_gui(self):
        if self.order_mode:
            self.food_2_up()
            self.update_food_count_labels()
            self.label_total.configure(text=(self.return_total_price_str()) + "€")
        else:
            self.new_serving[1] += 1
            self.update_food_count_labels()

    def food_3_up_gui(self):
        if self.order_mode:
            self.food_3_up()
            self.update_food_count_labels()
            self.label_total.configure(text=(self.return_total_price_str()) + "€")
        else:
            self.new_serving[2] += 1
            self.update_food_count_labels()

    def food_4_up_gui(self):
        if self.order_mode:
            self.food_4_up()
            self.update_food_count_labels()
            self.label_total.configure(text=(self.return_total_price_str()) + "€")
        else:
            self.new_serving[3] += 1
            self.update_food_count_labels()

    def food_1_down_gui(self):
        if self.order_mode:
            self.food_1_down()
            self.update_food_count_labels()
            self.label_total.configure(text=(self.return_total_price_str()) + "€")
        else:
            self.new_serving[0] -= 1
            self.update_food_count_labels()

    def food_2_down_gui(self):
        if self.order_mode:
            self.food_2_down()
            self.update_food_count_labels()
            self.label_total.configure(text=(self.return_total_price_str()) + "€")
        else:
            self.new_serving[1] -= 1
            self.update_food_count_labels()

    def food_3_down_gui(self):
        if self.order_mode:
            self.food_3_down()
            self.update_food_count_labels()
            self.label_total.configure(text=(self.return_total_price_str()) + "€")
        else:
            self.new_serving[2] -= 1
            self.update_food_count_labels()

    def food_4_down_gui(self):
        if self.order_mode:
            self.food_4_down()
            self.update_food_count_labels()
            self.label_total.configure(text=(self.return_total_price_str()) + "€")
        else:
            self.new_serving[3] -= 1
            self.update_food_count_labels()


    def return_total_price_str(self):
        price = 0
        for i in range(4):
            price += self.current_order[i] * self.food_prices[i]
        return str(price)


    def update_food_count_labels(self):
        if self.order_mode:
            food_counts = self.return_current_order_str().split(' ')
            self.label_food_1.configure(text=food_counts[0])
            self.label_food_2.configure(text=food_counts[1])
            self.label_food_3.configure(text=food_counts[2])
            self.label_food_4.configure(text=food_counts[3])
        else:
            self.label_food_1.configure(text=self.new_serving[0])
            self.label_food_2.configure(text=self.new_serving[1])
            self.label_food_3.configure(text=self.new_serving[2])
            self.label_food_4.configure(text=self.new_serving[3])


    def submit_serving_gui(self):
        self.submit_new_serving(self.new_serving)
        self.label_ordered.configure(text=self.count_current_orders_str())
        self.new_serving = [0, 0, 0, 0]
        self.update_food_count_labels()


    def previous(self):
        self.previous_order()
        self.label_queue_number.configure(text=str(self.return_queue_number()))
        self.update_food_count_labels()
        self.label_total.configure(text=(self.return_total_price_str()) + "€")


    def next(self):
       self.next_order()
       self.label_queue_number.configure(text=str(self.return_queue_number()))
       self.update_food_count_labels()
       self.label_total.configure(text=(self.return_total_price_str()) + "€")





    def exit(self):
        self.main_window.destroy()