from tkinter import *
import sqlite3

root = Tk()
root.title('database app')
root.geometry("390x500")  # initial size of the window

# databases

# create table
# c.execute("""CREATE TABLE addresses (
#     first_name text,
#     last_name text,
#     address text,
#     city text,
#     state text,
#     zipcode integer
#     )""")


# create edit function to update a record
def update():
    # create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # create cursor
    c = conn.cursor()

    record_id = select_box.get()

    c.execute("""UPDATE addresses SET
    first_name = :first,
    last_name = :last,
    city = :city,
    state = :state,
    zipcode = :zipcode
    
    WHERE oid = :oid""",
              {'first': f_name_editor.get(),
               'last': l_name_editor.get(),
               'address': address_editor.get(),
               'city': city_editor.get(),
               'state': state_editor.get(),
               'zipcode': zipcode_editor.get(),

               'oid': record_id
              })

    # commit changes
    conn.commit()

    # close connection
    conn.close()

    editor.destroy()
    select_box.delete(0, END)


# create edit function to update a record
def edit():
    global editor

    editor = Tk()
    editor.title('update a record')
    editor.geometry("390x220")

    # create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # create cursor
    c = conn.cursor()

    record_id = select_box.get()

    # query the database
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()

    # create global variables for text box names
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # create text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    # create text box labels
    f_name_label_editor = Label(editor, text="first name")
    f_name_label_editor.grid(row=0, column=0, pady=(10, 0))
    l_name_label_editor = Label(editor, text="last name")
    l_name_label_editor.grid(row=1, column=0)
    address_label_editor = Label(editor, text="address")
    address_label_editor.grid(row=2, column=0)
    city_label_editor = Label(editor, text="city")
    city_label_editor.grid(row=3, column=0)
    state_label_editor = Label(editor, text="state")
    state_label_editor.grid(row=4, column=0)
    zipcode_label_editor = Label(editor, text="zipcode")
    zipcode_label_editor.grid(row=5, column=0)

    #loop thru results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # create an save button to save edited record
    save_btn = Button(editor, text="save record", command=update)
    save_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=145)


# create function to delete a record
def delete():
    # create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # create cursor
    c = conn.cursor()

    # delete a record
    c.execute("DELETE from addresses WHERE oid= " + select_box.get())

    # commit changes
    conn.commit()

    # close connection
    conn.close()

    select_box.delete(0, END)


# create submit function for database
def submit():
    # create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # create cursor
    c = conn.cursor()

    # insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })

    # commit changes
    conn.commit()

    # close connection
    conn.close()

    # clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


# create query function
def query():
    global query_label

    query_label.grid_forget()

    # create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # create cursor
    c = conn.cursor()

    # query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    # print(records)

    # loop thru results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    # commit changes
    conn.commit()

    # close connection
    conn.close()


# create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)
select_box = Entry(root, width=30)
select_box.grid(row=9, column=1, pady=(20, 0))


# create text box labels
f_name_label = Label(root, text="first name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="last name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="city")
city_label.grid(row=3, column=0)
state_label = Label(root, text="state")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="zipcode")
zipcode_label.grid(row=5, column=0)
select_box_label = Label(root, text="select ID")
select_box_label.grid(row=9, column=0, pady=(20, 0))


# create submit button
submit_btn = Button(root, text="add record to database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# create a query button
query_btn = Button(root, text="show records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# create a delete button
delete_btn = Button(root, text="delete record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# create an edit button
edit_btn = Button(root, text="edit record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=144)

# blank space to show records later
query_label = Label(root, text=" ")
query_label.grid(row=12, column=0, columnspan=2)


root.mainloop()
