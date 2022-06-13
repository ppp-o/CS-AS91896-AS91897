

from tkinter import *

#quit function 
def quit():
    main_window.destroy()

#print details of the store
def print_store_details ():
    global total_entries, item_count
    item_count = 0
    Label(main_window, font='bold',text="Julie's Party Hire").grid(column=0,row=7)
    Label(main_window, font='bold',text="Customers Full Name").grid(column=1,row=7)
    Label(main_window, font='bold',text="Receipt Number").grid(column=2,row=7)
    Label(main_window, font='bold',text="Item Hired").grid(column=3,row=7)
    Label(main_window, font='bold',text="Number of Items Hired").grid(column=4,row=7)

    while item_count < total_entries :
        Label(main_window, text=item_count).grid(column=0,row=item_count+8) 
        Label(main_window, text=(store_details[item_count][0])).grid(column=1,row=item_count+8)
        Label(main_window, text=(store_details[item_count][1])).grid(column=2,row=item_count+8)
        Label(main_window, text=(store_details[item_count][2])).grid(column=3,row=item_count+8)
        Label(main_window, text=(store_details[item_count][3])).grid(column=4,row=item_count+8)
        item_count +=  1

