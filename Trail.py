from tkinter import * 
from tkinter import ttk 

root= Tk()

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
          text="Recipt number").grid(column=2, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Item hired").grid(column=3, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="NUmber of iteams").grid(column=4, row=7)




