from tkinter import * 
from tkinter import ttk 

root= Tk()

#quit subroutine
def quit():
    main_window.destroy()

def print_Julies_party_hire_details():
    # these are the global variables that are used
    global j_names, total_entries, name_count
    name_count = 0
    # Create the column headings
    Label(main_window, font=("Helvetica 10 bold"),
          text="Row").grid(column=0, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Customer full name").grid(column=1, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Item hired").grid(column=2, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Number of items").grid(column=3, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Recipt number").grid(column=4, row=7) 

# adding in each item into the list row
    while name_count < total_entries:
        Label(main_window, text=name_count).grid(column=0, row=name_count+8)
        Label(main_window, text=(Julies_party_hire_details[name_count][0])).grid(
            column=1, row=name_count+8)
        Label(main_window, text=(Julies_party_hire_details[name_count][1])).grid(
            column=2, row=name_count+8)
        Label(main_window, text=(Julies_party_hire_details[name_count][2])).grid(
            column=3, row=name_count+8)
        Label(main_window, text=(Julies_party_hire_details[name_count][3])).grid(
            column=4, row=name_count+8)
        name_count += 1

#createing buttons and labels for the gui
def setup_buttons():
    global Julies_party_hire_details, entry_Customer_full_name,entry_Item_hired,entry_recipt_number,entry_weather, total_entries, delete_item
    Button(main_window, text="Quit",command=quit) .grid(column=1, row=0)
    Button(main_window, text="Append Details",command=append_name) .grid(column=0,row=1)
    Button(main_window, text="Print Details",command=print_Julies_party_hire_details) .grid(column=1,row=1)
    Label(main_window, text="Customer full name") .grid(column=0,row=2)
    entry_Customer_full_name = Entry(main_window)
    entry_Customer_full_name.grid(column=1,row=2)
    Label(main_window, text="Item hired") .grid(column=0,row=3)
    entry_Item_hired = Entry(main_window)
    entry_Item_hired.grid(column=1,row=3)
    Label(main_window, text="Recipt number") .grid(column=0,row=4)
    entry_campers = Entry(main_window)
    entry_campers.grid(column=1,row=4)
    Label(main_window, text="Number of items") .grid(column=0,row=5)
    entry_Number_of_items = Entry(main_window)
    entry_Number_of_items.grid(column=1,row=5)
    Label(main_window, text="Row #") .grid(column=0,row=6)
    delete_item = Entry(main_window)
    delete_item .grid(column=1,row=6)
    Button(main_window, text="Delete",command=delete_row) .grid(column=2,row=6)






