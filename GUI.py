# coding=utf-8

from tkinter import *
from OrderHistory import *
from Bluetooth import *


class GUI(OrderHistory):
    def __init__(self):
        super().__init__()
        self.bt = Bluetooth()
        self.main_window = Tk()
        self.order_mode = True
        self.food_names = ["Lihis", "Ranut", "Makkaraperunat", "Sipulirenkaat", "Kinkkupizza", "Salamipizza",
                           "Mozzarellapizza", "Mozzarellatikut"]
        self.food_prices = [3.0, 2.0, 3.0, 2.0, 1.0, 1.0, 1.0, 5.0]
        self.new_serving = 0

        # Row 0
        self.button_order = Button(self.main_window, text="Vastaanota\ntilauksia", background="green", state=DISABLED,
                                   command=self.order, width=15)
        self.button_serve = Button(self.main_window, text="Tarjoile ruokia", background="grey", command=self.serve,
                                   width=15, height=2)
        self.label_queue_number_text = Label(self.main_window, text="Vuoronumero:", width=15)
        self.label_queue_number = Label(self.main_window, text=str(self.return_queue_number()), width=10, font=("", 12))
        self.label_ordered_foods = Label(self.main_window, text="Tilatut ruuat:", width=15)
        self.label_ordered = Label(self.main_window, text=self.count_current_orders_str(), width=15)
        self.button_order.grid(row=0, column=0)
        self.button_serve.grid(row=0, column=1)
        self.label_queue_number_text.grid(row=0, column=2)
        self.label_queue_number.grid(row=0, column=3, sticky=W)
        self.label_ordered_foods.grid(row=0, column=8)
        self.label_ordered.grid(row=0, column=9)
        self.label_order_history = Label(self.main_window, text="Tilaushistoria:")
        self.label_order_history.grid(row=0, column=10, sticky=W)

        # Row 1
        self.label_spacer_1 = Label(self.main_window, text=" ")
        self.label_spacer_1.grid(row=1, column=0)
        self.order_history_field = Text(height=30, width=45)
        self.scrollbar = Scrollbar()
        self.order_history_field.grid(row=1, column=10, rowspan=10, sticky=N + S)
        self.scrollbar.grid(row=1, column=11, rowspan=10, sticky=N + S)
        self.scrollbar.configure(command=self.order_history_field.yview)
        self.order_history_field.configure(yscrollcommand=self.scrollbar.set)

        # Row 2
        self.label_food_1_text = Label(self.main_window, text=self.food_names[0]
            + ": " + str(self.food_order_count(0)), width=15)
        self.label_food_2_text = Label(self.main_window, text=self.food_names[1]
            + ": " + str(self.food_order_count(1)), width=15)
        self.label_food_3_text = Label(self.main_window, text=self.food_names[2]
            + ": " + str(self.food_order_count(2)), width=15)
        self.label_food_4_text = Label(self.main_window, text=self.food_names[3]
            + ": " + str(self.food_order_count(3)), width=15)
        self.label_food_1_text.grid(row=1, column=0)
        self.label_food_2_text.grid(row=1, column=1)
        self.label_food_3_text.grid(row=1, column=2)
        self.label_food_4_text.grid(row=1, column=3)
        self.food_text_entrys = []
        self.food_text_entrys.append(self.label_food_1_text)
        self.food_text_entrys.append(self.label_food_2_text)
        self.food_text_entrys.append(self.label_food_3_text)
        self.food_text_entrys.append(self.label_food_4_text)

        # Row 3
        self.button_food_1 = Button(self.main_window, text="↑", command=lambda: self.select_food(1), width=2, height=1, font=("", 40))
        self.button_food_2 = Button(self.main_window, text="↑", command=lambda: self.select_food(2), width=2, height=1, font=("", 40))
        self.button_food_3 = Button(self.main_window, text="↑", command=lambda: self.select_food(3), width=2, height=1, font=("", 40))
        self.button_food_4 = Button(self.main_window, text="↑", command=lambda: self.select_food(4), width=2, height=1, font=("", 40))
        self.button_food_1.grid(row=3, column=0)
        self.button_food_2.grid(row=3, column=1)
        self.button_food_3.grid(row=3, column=2)
        self.button_food_4.grid(row=3, column=3)
        self.food_buttons = []
        self.food_buttons.append(self.button_food_1)
        self.food_buttons.append(self.button_food_2)
        self.food_buttons.append(self.button_food_3)
        self.food_buttons.append(self.button_food_4)

        # Row 4
        self.entry_food_1_price = Entry(self.main_window, width=6, justify=CENTER)
        self.entry_food_2_price = Entry(self.main_window, width=6, justify=CENTER)
        self.entry_food_3_price = Entry(self.main_window, width=6, justify=CENTER)
        self.entry_food_4_price = Entry(self.main_window, width=6, justify=CENTER)
        self.entry_food_1_price.insert(0, str(self.food_prices[0]))
        self.entry_food_2_price.insert(0, str(self.food_prices[1]))
        self.entry_food_3_price.insert(0, str(self.food_prices[2]))
        self.entry_food_4_price.insert(0, str(self.food_prices[3]))
        self.entry_food_1_price.grid(row=4, column=0)
        self.entry_food_2_price.grid(row=4, column=1)
        self.entry_food_3_price.grid(row=4, column=2)
        self.entry_food_4_price.grid(row=4, column=3)
        self.food_price_entrys = []
        self.food_price_entrys.append(self.entry_food_1_price)
        self.food_price_entrys.append(self.entry_food_2_price)
        self.food_price_entrys.append(self.entry_food_3_price)
        self.food_price_entrys.append(self.entry_food_4_price)

        # Row 5
        self.label_food_1_price = Label(self.main_window, text=str(self.food_prices[0]) + "€")
        self.label_food_2_price = Label(self.main_window, text=str(self.food_prices[1]) + "€")
        self.label_food_3_price = Label(self.main_window, text=str(self.food_prices[2]) + "€")
        self.label_food_4_price = Label(self.main_window, text=str(self.food_prices[3]) + "€")

        self.label_food_1_price.grid(row=5, column=0)
        self.label_food_2_price.grid(row=5, column=1)
        self.label_food_3_price.grid(row=5, column=2)
        self.label_food_4_price.grid(row=5, column=3)
        self.food_price_labels = []
        self.food_price_labels.append(self.label_food_1_price)
        self.food_price_labels.append(self.label_food_2_price)
        self.food_price_labels.append(self.label_food_3_price)
        self.food_price_labels.append(self.label_food_4_price)

        # Row 6
        self.label_spacer_2 = Label(self.main_window, text=" ")
        self.label_spacer_2.grid(row=6, column=0)

        # Row 7
        self.label_food_5_text = Label(self.main_window, text=self.food_names[4]
            + ": " + str(self.food_order_count(4)), width=15)
        self.label_food_6_text = Label(self.main_window, text=self.food_names[5]
            + ": " + str(self.food_order_count(5)), width=15)
        self.label_food_7_text = Label(self.main_window, text=self.food_names[6]
            + ": " + str(self.food_order_count(6)), width=15)
        self.label_food_8_text = Label(self.main_window, text=self.food_names[7]
            + ": " + str(self.food_order_count(7)), width=15)
        self.label_food_5_text.grid(row=7, column=0)
        self.label_food_6_text.grid(row=7, column=1)
        self.label_food_7_text.grid(row=7, column=2)
        self.label_food_8_text.grid(row=7, column=3)
        self.food_text_entrys.append(self.label_food_5_text)
        self.food_text_entrys.append(self.label_food_6_text)
        self.food_text_entrys.append(self.label_food_7_text)
        self.food_text_entrys.append(self.label_food_8_text)

        # Rows 8
        self.button_food_5 = Button(self.main_window, text="↑", command=lambda: self.select_food(5), width=2, height=1, font=("", 40))
        self.button_food_6 = Button(self.main_window, text="↑", command=lambda: self.select_food(6), width=2, height=1, font=("", 40))
        self.button_food_7 = Button(self.main_window, text="↑", command=lambda: self.select_food(7), width=2, height=1, font=("", 40))
        self.button_food_8 = Button(self.main_window, text="↑", command=lambda: self.select_food(8), width=2, height=1, font=("", 40))
        self.button_food_5.grid(row=8, column=0)
        self.button_food_6.grid(row=8, column=1)
        self.button_food_7.grid(row=8, column=2)
        self.button_food_8.grid(row=8, column=3)
        self.food_buttons.append(self.button_food_5)
        self.food_buttons.append(self.button_food_6)
        self.food_buttons.append(self.button_food_7)
        self.food_buttons.append(self.button_food_8)

        # Row 9
        self.entry_food_5_price = Entry(self.main_window, width=6, justify=CENTER)
        self.entry_food_6_price = Entry(self.main_window, width=6, justify=CENTER)
        self.entry_food_7_price = Entry(self.main_window, width=6, justify=CENTER)
        self.entry_food_8_price = Entry(self.main_window, width=6, justify=CENTER)
        self.entry_food_5_price.insert(0, str(self.food_prices[4]))
        self.entry_food_6_price.insert(0, str(self.food_prices[5]))
        self.entry_food_7_price.insert(0, str(self.food_prices[6]))
        self.entry_food_8_price.insert(0, str(self.food_prices[7]))
        self.entry_food_5_price.grid(row=9, column=0)
        self.entry_food_6_price.grid(row=9, column=1)
        self.entry_food_7_price.grid(row=9, column=2)
        self.entry_food_8_price.grid(row=9, column=3)
        self.food_price_entrys.append(self.entry_food_5_price)
        self.food_price_entrys.append(self.entry_food_6_price)
        self.food_price_entrys.append(self.entry_food_7_price)
        self.food_price_entrys.append(self.entry_food_8_price)
        self.button_submit = Button(self.main_window, text="Tarjoile", state=DISABLED, command=self.submit_serving_gui,
                                    width=15)
        self.button_submit.grid(row=9, column=8, sticky=S)

        # Row 10
        self.label_food_5_price = Label(self.main_window, text=str(self.food_prices[4]) + "€")
        self.label_food_6_price = Label(self.main_window, text=str(self.food_prices[5]) + "€")
        self.label_food_7_price = Label(self.main_window, text=str(self.food_prices[6]) + "€")
        self.label_food_8_price = Label(self.main_window, text=str(self.food_prices[7]) + "€")
        self.label_food_5_price.grid(row=10, column=0)
        self.label_food_6_price.grid(row=10, column=1)
        self.label_food_7_price.grid(row=10, column=2)
        self.label_food_8_price.grid(row=10, column=3)
        self.food_price_labels.append(self.label_food_5_price)
        self.food_price_labels.append(self.label_food_6_price)
        self.food_price_labels.append(self.label_food_7_price)
        self.food_price_labels.append(self.label_food_8_price)
        self.button_previous = Button(self.main_window, text="Edellinen", command=self.previous, width=15)
        self.button_next = Button(self.main_window, text="Seuraava", command=self.next, width=15)
        self.button_previous.grid(row=10, column=8)
        self.button_next.grid(row=10, column=9)
        ##

        self.update_order_history_field()
        self.main_window.mainloop()



    def order(self):
        """
        Change program state to ordering foods
        """

        self.button_order.configure(state=DISABLED, background="green")
        self.button_serve.configure(state=NORMAL, background="gray")
        self.toggle_mode()
        self.label_queue_number_text.configure(text="Vuoronumero:")
        self.label_queue_number.configure(text=str(self.return_queue_number()))

        for i in range(8):
            self.food_price_labels[i].configure(text=str(self.food_prices[i]) + "€")

        self.button_submit.configure(state=DISABLED)
        self.button_previous.configure(state=NORMAL)
        self.button_next.configure(state=NORMAL)
        self.update_logfile()
        self.update_order_history_field()


    def serve(self):
        """
        Change program state to serving foods
        """

        self.button_order.configure(state=NORMAL, background="grey")
        self.button_serve.configure(state=DISABLED, background="red")

        self.toggle_mode()
        self.new_serving = 0

        self.label_queue_number_text.configure(text="")
        self.label_queue_number.configure(text="")

        for label in self.food_price_labels:
            label.configure(text="")

        self.button_submit.configure(state=NORMAL)
        self.button_previous.configure(state=DISABLED)
        self.button_next.configure(state=DISABLED)
        self.update_logfile()
        self.update_order_history_field()


    def toggle_mode(self):
        """
        Toggle the mode from/to order mode. Reset button states during the change
        This method is called when a user changes the GUI view
        """

        for button in self.food_buttons:
            button.configure(state=NORMAL)
        if self.order_mode:
            self.order_mode = False
        else:
            self.order_mode = True


    def select_food(self, food_num):
        """
        Toggle all food buttons to active and then disable the one that was pressed
        This method is called when a user presses a food button
        """

        if self.order_mode:
            # In order mode the selected food is stored as the food on that order
            order_num = self.return_queue_number()

            # Only non served orders can be changed
            if not self.order_history[order_num].served:
                # Enable all buttons
                for i in range(8):
                    self.food_buttons[i].configure(state=NORMAL)
                # Disable current food button
                self.food_buttons[food_num - 1].configure(state=DISABLED)

                self.order_history[order_num].food = food_num
                self.order_history[order_num].food_name = self.food_names[food_num - 1]
        else:
            # Enable all buttons
            for i in range(8):
                self.food_buttons[i].configure(state=NORMAL)
            # Disable current food button
            self.food_buttons[food_num - 1].configure(state=DISABLED)

            self.new_serving = food_num



########################################################################################################################

    def return_total_price_str(self):
        return str(self.current_order)


    def submit_serving_gui(self):
        order_num = self.find_serving_number(self.new_serving)
        # If no servable order (should not happen)
        if order_num == 0:
            return
        self.popup(order_num)
        self.order_history[order_num].serving_time = time.strftime('%X')
        self.submit_new_serving(self.new_serving)

        self.update_awaiting_items()

        self.new_serving = 0
        self.update_order_history_field()
        for button in self.food_buttons:
            button.configure(state=NORMAL)
        self.update_logfile()
        self.bt.send_foods(self.count_current_orders())


    def popup(self, order_num):
        """
        Displays a popup message showing the number of the order that was
        served
        """

        popup = Toplevel()
        popup.title("!")

        message = Message(popup, text=str(order_num), font=("", 30))
        message.pack()

        button = Button(popup, text="Ok", command=popup.destroy)
        button.pack()


    def previous(self):
        """
        Select the previous order
        """

        self.previous_order()
        self.update_logfile()

        self.label_queue_number.configure(text=str(self.return_queue_number()))

        self.update_awaiting_items()

        self.update_order_history_field()

        # Enable all buttons
        for button in self.food_buttons:
            button.configure(state=NORMAL)
        # Disable button of ordered food
        food_num = self.order_history[self.return_queue_number()].food
        if food_num > 0:
            self.food_buttons[food_num-1].configure(state=DISABLED)


    def next(self):
        """
        Select the next order
        """

        self.next_order()
        self.update_logfile()

        self.label_queue_number.configure(text=str(self.return_queue_number()))

        self.update_awaiting_items()

        self.bt.send_foods(self.count_current_orders())
        self.update_order_history_field()

        # Enable all buttons
        for button in self.food_buttons:
            button.configure(state=NORMAL)
        # Disable button of ordered food
        food_num = self.order_history[self.return_queue_number()].food
        if food_num > 0:
            self.food_buttons[food_num-1].configure(state=DISABLED)

        #FIXME if this order has no food selected disable the next button in gui


    def update_order_history_field(self):
        """
        Update the gui element showing the order order history
        """

        # Clear text field
        self.order_history_field.delete(1.0, END)

        # Update the order history in gui
        for order in self.order_history:
            line = ""
            served = "F"
            if order.served:
                served = "T"
            food_name = order.food_name
            order_time = order.order_time
            serving_time = order.serving_time
            if serving_time == "":
                serving_time = "        "

            line += str(order.number) + "  " + str(order.food) + "  " + served + "  " + order_time + \
                    "  " + serving_time + "  " + food_name +'\n'

            # Insert the line to gui. Use a red color on the current order line
            # to emphasise it
            if self.current_queue_number == order.number:
                tag_name = "color-red"
                self.order_history_field.tag_configure(tag_name, foreground="red")
            else:
                tag_name = "color-black"
                self.order_history_field.tag_configure(tag_name, foreground="black")
            self.order_history_field.insert(END, line, tag_name)

        # Remove first row
        self.order_history_field.delete(1.0, 2.0) #XXX Why is it removed removed?
        # Scroll to the end
        self.order_history_field.see(END)

    def update_awaiting_items(self):
        """
        Update gui for the number of items awaiting to be served
        """

        self.label_ordered.configure(text=self.count_current_orders_str())

        food_index = 0
        for label in self.food_text_entrys:
            food_name = self.food_names[food_index]
            label.configure(text=food_name + ": " + str(self.food_order_count(food_index)))
            food_index += 1

    def exit(self):
        self.main_window.destroy()
