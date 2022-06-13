

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

#add the print_store_details to the list
def append_details ():
    global store_details, entry_customer_name,entry_receipt_number,entry_item_number,entry_item_hired, total_entries
    if len(entry_customer_name.get()) != 0 :
        store_details.append([entry_customer_name.get(),entry_receipt_number.get(),entry_item_number.get(),entry_item_hired.get()])
        entry_customer_name.delete(0,'end')
        entry_receipt_number.delete(0,'end')
        entry_item_number.delete(0,'end')
        entry_item_hired.delete(0,'end')
        total_entries +=  1