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
    # column headings
    Label(main_window, font=("Helvetica 10 bold"),
          text="Row").grid(column=0, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Customer full name").grid(column=1, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Recipt number").grid(column=2, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Item hired").grid(column=3, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Number of iteams").grid(column=4, row=7)

# add each item in the list into its own row
    while name_count < total_entries:
        Label(main_window, text=name_count).grid(column=0, row=name_count+8)
        Label(main_window, text=(camp_details[name_count][0])).grid(
            column=1, row=name_count+8)
        Label(main_window, text=(camp_details[name_count][1])).grid(
            column=2, row=name_count+8)
        Label(main_window, text=(camp_details[name_count][2])).grid(
            column=3, row=name_count+8)
        Label(main_window, text=(camp_details[name_count][3])).grid(
            column=4, row=name_count+8)
        name_count += 1

main()




