import random
import msvcrt

class RemoteControl():

    def __init__(self, tv_state="Off", tv_volume=0, channel_list=["Trt"], channel="Trt"):
        print("Remote Control is being created...")

        self.tv_volume = tv_volume
        self.tv_state = tv_state
        self.channel_list = channel_list
        self.channel = channel

    def adjust_volume(self):

        while True:
            char = input("Press '<' to decrease, '>' to increase, 'q' to finish")

            if char == "<":
                if self.tv_volume != 0:
                    self.tv_volume -= 1
                    print("Volume:", self.tv_volume)
            elif char == ">":
                if self.tv_volume != 32:
                    self.tv_volume += 1
                    print("Volume:", self.tv_volume)
            else:
                print("Volume Updated:", self.tv_volume)
                break

    def turn_off_tv(self):
        print("TV is turning off.")

        self.tv_state = "Off"

    def turn_on_tv(self):
        print("TV is turning on.")
        self.tv_state = "On"

    def __str__(self):
        return "TV State: {}\nVolume: {}\nChannels: {}\nCurrent Channel: {}\n".format(self.tv_state, self.tv_volume, self.channel_list, self.channel)

    def __len__(self):
        return len(self.channel_list)

    def random_channel(self):
        random_channel = random.randint(0, len(self.channel_list)-1)

        self.channel = self.channel_list[random_channel]

        print("Current Channel:", self.channel)

    def add_channel(self, new_channel):
        print("Channel Added ", new_channel)
        self.channel_list.append(new_channel)


remote_control = RemoteControl()
print("""*******************

TV Application

Operations;

1. Turn on TV

2. Turn off TV

3. TV Information

4. Number of Channels

5. Add Channel

6. Switch to a Random Channel

7. Adjust Volume
To exit, press 'q'.
*******************""")

while True:

    operation = input("Choose an operation:")
    if operation == "q":
        print("Exiting the Program...")
        break
    if operation == "1":
        remote_control.turn_on_tv()
    elif operation == "2":
        remote_control.turn_off_tv()
    elif operation == "3":
        print(remote_control)
    elif operation == "4":
        print("Number of Channels: ", len(remote_control))
    elif operation == "5":
        channels = input("Enter the channels you want to add, separated by ',':")
        to_add = channels.split(",")
        for i in to_add:
            remote_control.add_channel(i)
        print("Channel List Successfully Updated.")
    elif operation == "6":
        remote_control.random_channel()
    elif operation == "7":
        remote_control.adjust_volume()
    else:
        print("Invalid Operation...")
