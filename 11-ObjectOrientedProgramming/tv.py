# tv.py file
# class definition
class TV:
    def __init__(self):
        self.is_on = False
        self.channel = 1
        self.channels_list = []

    def turn_off(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True   

    def show_status(self):
        if self.is_on:
            if len(self.channels_list) == 0:
                print(f"TV is on, channel {self.channel} ")
            else:
                print(f"TV is on, channel {self.channel} ({self.channels_list[self.channel - 1]})")
        else:
            print("TV is off")
    def set_channel(self,new_channel_no):
        if self.is_on:
            self.channel = new_channel_no
    
    def set_channels(self, channels):
        x = channels.split()
        for i in x:
            self.channels_list.append(i)

    def show_channels(self):
        print("Channel list:")
        for i in range(len(self.channels_list)):
            print(f"{i+1}. {self.channels_list[i]}")