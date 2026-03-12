from tkinter import *
from tkinter import messagebox
import random as rd
import pyperclip 
import json 
import os
from dotenv import load_dotenv


load_dotenv()

FONT_NAME = "Arial"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []

    for i  in range(rd.randint(8, 10)) :
         password_list.extend(rd.choice(letters))
    for i in range(rd.randint(2, 4)):
         password_list.extend(rd.choice(numbers))
    for i in range(rd.randint(2, 4)):
         password_list.extend(rd.choice(symbols))

    rd.shuffle(password_list)
    password="".join(password_list)
    password_box.insert(0, password)
    pyperclip.copy(password)

    
    

    

         
# ---------------------------- SAVE PASSWORD ------------------------------- #
def fetch_detail():
    Website_name = website_box.get()
    Email = user_email_box.get()
    Password = password_box.get()

    if (len(Website_name) and len(Password)) == 0:
            messagebox.showerror(title= "⚠ Warrning", message= "You have not entered Website name or Password")
            return

    add_details= messagebox.askokcancel(title= "⚠ Warrning", message= f"Are you suer to add these details\nWebsite: {Website_name}\nEmail: {Email}\nPassword: {Password}")
    new_data = {
        Website_name: {
              "Email": Email,
              "Password": Password
        }
    }

    if add_details :
        try:
            with open("Detail.json", "r") as data_file:
                #  Getting the previous data 
                data = json.load(data_file)
                # Updateting with new data
                data.update(new_data)

        except FileNotFoundError:        
            with open("Detail.json","w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("Detail.json","w") as data_file:
                json.dump(data, data_file, indent=4)
            
        website_box.delete(0, END)
        password_box.delete(0, END)
    else: 
        website_box.delete(0, END)
        password_box.delete(0, END)


# ---------------------------- SEARCH  ------------------------------- #
def search():
    Website_name = website_box.get()
    try:
        with open("Detail.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError :
        messagebox.showerror(title= "FILE ERROR", message = "File does not exist\n Try to save the first password")
    else:
        if Website_name in data :
            messagebox.showinfo(title = "FOUND", message = f"Website: {Website_name}\nEmail: {data[Website_name]["Email"]}\nPassword: {data[Website_name]["Password"]}")
        else:
            messagebox.showerror(title="NOT FOUND", message= " Data not found.")



# ---------------------------- UI SETUP ------------------------------- #
 #WINDOW CONTROLS
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

 # CANVAS CONTROLS
canvas = Canvas(width= 200, height= 200)
PASSWORD_IMAGE = PhotoImage(file= "logo.png")
canvas.create_image(100, 100 ,image=PASSWORD_IMAGE)
canvas.grid(column=1, row=0)

 #ENTRIES BOXWES AND LABLE WORK
website = Label(text= "Website: ", font=(FONT_NAME, 12))
website.grid(column=0, row= 1)
website_box = Entry(width=35)
website_box.grid(row=1,column=1, columnspan=2)
website_box.focus()

user_email= Label(text="Email/Username: ", font= (FONT_NAME, 12))
user_email.grid(column=0, row=2)
user_email_box = Entry(width=35)
user_email_box.insert(0,os.environ.get("Email"))
user_email_box.grid(row=2, column=1, columnspan=2)

password = Label(text = "Password: ", font= (FONT_NAME, 12))
password.grid(column=0, row= 3)
password_box = Entry(width=35)
password_box.grid(column=1, row= 3, columnspan=2)

#  #BUTTON
generate_button = Button(text="Generate Password",width=14, command= password_generator)
generate_button.grid(column=4, row=3,)

add_button = Button(text="Add", width=36, command= fetch_detail)
add_button.grid(column=1, row=4, columnspan=3 )

search = Button(text= "Search", width= 14, command= search)
search.grid(column= 4, row=1 )



window.mainloop()