"""
A program that stores book information
Title, Author
Year, ISBN

The user can:

View all records
Search an entry
Add an entry
Update an entry
Delete an entry
Close the program

"""
from tkinter import *
from backend import Database

database=Database("books.db")                 # we create an object, based on the Database class(the class is a blueprint for the object)

# Create an empty Tkinter window

def get_selected_row(event):                  # function is tied to an event
    try:                                      # if the list is empty and you click in it, it returns an "IndexError" because the is nothig selected, ergo no index;
                                              # this is why the "try" function is needed; it tries to execute the code under it, except the case of "IndexError"
        global  selected_tuple                # creates a global variable within the function
        index=list1.curselection()[0]         # points to the index of the selected entry; [0] is needed because the output is a tuple, and we need just the first item from the tuple
        selected_tuple=list1.get(index)       # returns the tuple with index 1 from the listbox
        e1.delete(0,END)                      # clears the entry field for the "Title" from the beginning to the END of the row
        e1.insert(END,selected_tuple[1])      # inserts in the entry field, at the END of the row (which now is the BEGINNING :) ), the title of the selected book 
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)                      
        e3.insert(END,selected_tuple[3])          
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)               # it empties the list before adding the selection;
                                      # in this way you don't have the same selection added in the list when you press the "View all" button multiple times
    for row in database.view():        # the new row will be put at the end of the previous row;
        list1.insert(END,row)         # the first row will be first because it has no previous row  

def search_command():
     list1.delete(0,END)
     for row in database.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row) 

def add_command(): 
    database.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())       
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def delete_command():
    database.delete(selected_tuple[0])

def update_command():
    database.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

window=Tk()

window.wm_title("Bookstore")

#######################################
############### Labels ################
#######################################

# Create label widget called "Title"
l1=Label(window, text="Title")
l1.grid(row=0,column=0)

# Create label widget called "Author"
l2=Label(window, text="Author")
l2.grid(row=0,column=2)

# Create label widget called "Year"
l3=Label(window, text="Year")
l3.grid(row=1,column=0)

# Create label widget called "ISBN"
l4=Label(window, text="ISBN")
l4.grid(row=1,column=2)

########################################
############### Entries ################
########################################

# Create empty entry box
title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

# Create empty entry box
author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

# Create empty entry box
year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

# Create empty entry box
isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

########################################
######## Listbox with scrollbar ########
########################################
list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)  # binds an event type <<ListboxSelect>> to a function, so it applies the function for the selected row from the list

########################################
############ Button widgets ############
########################################

b1=Button(window,text="View all",width=12,command=view_command)   # the function "view_command" doesn't need "()"; 
b1.grid(row=2,column=3)                                           # if it had "()" it would run the function with the program, not when the button is pressed

b2=Button(window,text="Search entry",width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry",width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update selected",width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete selected",width=12,command=delete_command)
b5.grid(row=6,column=3) 

b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()