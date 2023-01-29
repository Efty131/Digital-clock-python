import time
from datetime import datetime
from pytz import timezone
from tkinter import *

root = Tk()
root.geometry("359x150+0+0")
root.configure(background="black") 
# root.overrideredirect(1)

bd_tz = timezone("Asia/Dhaka")

def start():
    current_date = datetime.now(bd_tz).strftime("%B %d, %Y")
    current_time = datetime.now(bd_tz).strftime("%I:%M:%S %p")
    label_date.config(text = current_date)
    label_time.config(text = current_time)
    label_time.after(200,start)

label_time = Label(root, font=("ds-digital",50,'bold'),bg="black",fg="aqua",bd=50)
label_time.grid(row=1,column=1)
label_date = Label(root, font=("ds-digital",20,'bold'),bg="black",fg="blue",bd=50)
label_date.grid(row=0,column=1)

start()
print("Done")
root.mainloop()