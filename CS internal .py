from tkinter import *

#quit subroutine
def quit():
    main_window.destroy()

#print details of the store
def print_store_details ():
    global total_entries, item_count
    item_count = 0
    Label(main_window, font='bold',text="Row").grid(column=0,row=7)
    Label(main_window, font='bold',text="Customers Full Name").grid(column=1,row=7)
    Label(main_window, font='bold',text="Receipt Number").grid(column=2,row=7)
    Label(main_window, font='bold',text="Number of Items Hired").grid(column=3,row=7)
    Label(main_window, font='bold',text="Item Hired").grid(column=4,row=7)

    while item_count < total_entries :
        Label(main_window, text=item_count).grid(column=0,row=item_count+8) 
        Label(main_window, text=(store_details[item_count][0])).grid(column=1,row=item_count+8)
        Label(main_window, text=(store_details[item_count][1])).grid(column=2,row=item_count+8)
        Label(main_window, text=(store_details[item_count][2])).grid(column=3,row=item_count+8)
        Label(main_window, text=(store_details[item_count][3])).grid(column=4,row=item_count+8)
        item_count +=  1


def check_inputs():
    # these are the global variables that are used
    global store_details, entry_customer_name, entry_receipt_number, entry_item_hired, entry_item_number, total_entries
    input_check = 0.
    Label(main_window, text="                                      ") .grid(column=2, row=2)
    Label(main_window, text="                                      ") .grid(column=2, row=3)
    Label(main_window, text="                                      ") .grid(column=2, row=4)
    Label(main_window, text="                                      ") .grid(column=2, row=5)
    # Check that Customers_Full_Name is not blank, set error text if blank
    if len(entry_customer_name.get()) == 0:
        Label(main_window, fg="red", text="Required/letters only") .grid(column=2, row=2)
        input_check = 1
    # Check that Item_Hired is not blank, set error text if blank
    if len(entry_item_hired.get()) == 0:
        Label(main_window, fg="red", text="Required/letters only") .grid(column=2, row=4)
        input_check = 1
    if len(entry_item_number.get()) == 0:
        Label(main_window, fg="red", text="Required") .grid(column=2, row=5)
        input_check = 1
    # Check the Number_of_Items_Hired is not blank and between 1 and 500, set error text if blank
    if (entry_item_number.get().isdigit()):
        if int(entry_item_number.get()) < 1 or int(entry_item_number.get()) > 500:
            Label(main_window, fg="red", text="1-500 only") .grid(column=2, row=5)
            input_check = 1
        else:
            pass
    else:
        Label(main_window, fg="red", text="Required/1-500") .grid(column=2, row=5)
        input_check = 1
    # Check that Receipt Number is not blank, set error text if blank
    if len(entry_receipt_number.get()) == 0:
        Label(main_window, fg="red", text="Required/number only") .grid(column=2, row=3)
        input_check = 1
    if input_check == 0:
        append_details()

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

#deleteing a row from the list
def delete_row ():
    global store_details, delete_item, total_entries, item_count
    del store_details[int(delete_item.get())]
    total_entries = total_entries - 1
    delete_item.delete(0,'end')  
    Label(main_window, text="                                          ").grid(column=0,row=item_count+7) 
    Label(main_window, text="                                          ").grid(column=1,row=item_count+7)
    Label(main_window, text="                                          ").grid(column=2,row=item_count+7)
    Label(main_window, text="                                          ").grid(column=3,row=item_count+7)
    Label(main_window, text="                                          ").grid(column=4,row=item_count+7)
    print_store_details()

#createing the buttons and labels
def setup_buttons():
    global store_details, entry_customer_name,entry_receipt_number,entry_item_number,entry_item_hired, total_entries, delete_item
    Button(main_window, text="Quit",command=quit) .grid(column=3, row=1)
    Button(main_window, text="Append Details",command=check_inputs) .grid(column=0,row=1)
    Button(main_window, text="Print Details",command=print_store_details) .grid(column=1,row=1)
    Label(main_window, text="Customer Full Name") .grid(column=0,row=2)
    entry_customer_name = Entry(main_window)
    entry_customer_name.grid(column=1,row=2)
    Label(main_window, text="Receipt Number") .grid(column=0,row=3)
    entry_receipt_number = Entry(main_window)
    entry_receipt_number.grid(column=1,row=3)
    Label(main_window, text="Item Hired") .grid(column=0,row=4)
    entry_item_hired = Entry(main_window)
    entry_item_hired.grid(column=1,row=4)
    Label(main_window, text="Number of Item/s Hired") .grid(column=0,row=5)
    entry_item_number = Entry(main_window)
    entry_item_number.grid(column=1,row=5)
    Label(main_window, text="Row #") .grid(column=0,row=6)
    delete_item = Entry(main_window)
    delete_item .grid(column=1,row=6)
    Button(main_window, text="Delete row",command=delete_row) .grid(column=2,row=6)



#start the program running
def main():
    global main_window
    global store_details, total_entries
    store_details = []
    total_entries = 0
    main_window =Tk()
    main_window.title("Julie's Party Hire")
    setup_buttons()
    main_window.mainloop()
    
main()







