# import time
# from datetime import datetime
# from pytz import timezone
# from tkinter import *

# root = Tk()
# root.geometry("359x150+0+0")
# root.configure(background="black")
# root.resizable(0,0)
# # root.overrideredirect(1)  [this line is to hide the title bar ]

# # Set the timezone to Bangladesh
# bd_tz = timezone("Asia/Dhaka")

# # Function that updates the time label
# def start():
#     text = datetime.now(bd_tz).strftime("%H:%M:%S")
#     label.config(text = text)
#     label.after(200,start)

# # Create a time label
# label = Label(root,font=("ds-digital",50,'bold'),bg="black",fg="aqua",bd=50)
# label.grid(row=0,column=1)

# # Start the update loop
# start()
# print("Clock is running")
# root.mainloop()
import time
from datetime import datetime
from pytz import timezone
from tkinter import *

root = Tk()
root.geometry("359x150+0+0")
root.configure(background="black")
# root.resizable(0,0)
# root.overrideredirect(1)

bd_tz = timezone("Asia/Dhaka")

def start():
    text = datetime.now(bd_tz).strftime("%I:%M:%S %p")
    label.config(text = text)
    label.after(200,start)

label = Label(root,font=("ds-digital",50,'bold'),bg="black",fg="aqua",bd=50)
label.grid(row=0,column=1)
start()
root.mainloop()
