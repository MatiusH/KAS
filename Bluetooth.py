import serial
import serial.tools.list_ports


class Bluetooth:
    def __init__(self):
        try:
            # Find the serial port the bluetooth module is connected to
            #ports = list(serial.tools.list_ports.comports())
            # bluetooth_port = ""
            # for p in ports:
            #     if p[2] == "USB VID:PID=1a86:7523":
            #         bluetooth_port = p[0]
            #         print(bluetooth_port)
            # if bluetooth_port == "":
            #     raise serial.SerialException

            self.ser = serial.Serial()
            self.ser.baudrate = 38400
            # self.ser.port = bluetooth_port
            self.ser.port = "/dev/ttyUSB1"
            #self.ser.timeout = 0.1      # Timeout to wait for response
            self.ser.xonxoff = False    # Disable software flow control
            self.ser.dsrdtr = False     # Disable hardware (DSR/DTR) flow control
            self.ser.rtscts = False     # Disable hardware (RTS/CTS) flow control
            self.ser.open()
            while not self.ser.isOpen():
                pass
        except serial.SerialException:
            print("USB-error")


    def send_foods(self, food_list):
        # Convert list of foods into a numbered string, in which each food
        # is represented by a single digit. If more than 9 foods are ordered,
        # 9 are shown on the screen.
        line = ""
        for i in range(len(food_list)):
            if food_list[i] > 9:
                line += " 9"
            else:
                line += ' ' + str(food_list[i])
        # Convert to nytes and sent to bluetooth module
        self.ser.write(line.encode())
        print(line)


    def close(self):
        self.ser.close()