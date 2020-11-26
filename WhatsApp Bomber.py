# WhatsApp Bomber
# Created by RH Tasin

import time
from os import name
import tkinter as tk
from tkinter import *
from logging import root
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def bombingTriger():
    target = str(name.get())
    msg = str(message.get())
    number = msgCount.get()
    driver = webdriver.Chrome('/home/tasin/Documents/chromedriver')
    driver.get('https://web.whatsapp.com/')

    time.sleep(20)
    user=driver.find_element_by_xpath('//span[@title = "'+target+'"]')
    user.click()

    msg_box=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    for i in range(number):
        msg_box.send_keys(msg)
        msg_box.send_keys(Keys.ENTER)


# Window start from here
window = tk.Tk()
window.title('WhatsApp Bomber')
window.geometry('450x400') 
window.resizable(width = False, height = False)
window.configure(bg='blue')

heading_label = Label(window, text = 'You have 20 secounds to scan and login', font = ('BatmanForeverAlternate', 12, 'bold'))
heading_label.place(x = 230, y = 15, anchor = 'center')

# Target name lebel
Label(window, text = 'Enter Name').place(x = 120, y = 80)
name = StringVar()
nameBox = Entry(window, textvariable = name).place(x = 230, y = 80)

# Message lebel
Label(window, text = 'Enter Message').place(x = 120, y = 150)
message = StringVar()
msgBox = Entry(window, textvariable = message).place(x = 230, y = 150)

Label(window, text = 'Threads').place(x = 120, y = 220)
msgCount = IntVar()
countBox = Entry(window, textvariable = msgCount).place(x = 230, y = 220)

# Push Button
tk.Button(window, text = 'Start Bombing', command = bombingTriger).place(x = 230, y = 300, anchor = 'center')
window.mainloop() 





