import tkinter
from tkinter import messagebox
from pass_gen import PasswordGenerator
from nikname_gen import NameGenerator

MY_EMAIL = "my_email007@mail.ru"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_gen = PasswordGenerator()
    new_password = password_gen.create()
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, new_password)

def nickname_generator():
    nick_gen = NameGenerator()
    new_name = nick_gen.name
    email_entry.delete(0, tkinter.END)
    email_entry.insert(0, new_name)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="EMPTY", message=f"There is nothing in one of the entry.\n"
                                                    f"Please, fill all of the fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered:\nEmail: {email}\n"
                                                              f"Password: {password}\nIs it OK to save?")
        if is_ok:
            with open("data.txt", "a+") as file:
                file.write(f"{website} | {email} | {password}\n")


# ---------------------------- UI SETUP ------------------------------- #


WIDTH = 40

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
window.geometry("440x440")
canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
lock_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# LABELS
website_label = tkinter.Label(text="Website:", anchor="nw")
website_label.grid(column=0, row=1)

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

# ENTRIES
website_entry = tkinter.Entry(width=WIDTH)
website_entry.insert(0, "Amazon")
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_entry = tkinter.Entry(width=WIDTH)
email_entry.insert(0, MY_EMAIL)
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = tkinter.Entry(width=WIDTH)
password_entry.insert(0, "****")
password_entry.grid(column=1, row=3, columnspan=2)

# BUTTONS
generate_button = tkinter.Button(text="Generate Password", command=password_generator)
generate_button.grid(column=1, row=4)
name_gen_button = tkinter.Button(text="Generate Nickname", command=nickname_generator)
name_gen_button.grid(column=1, row=5)

add_button = tkinter.Button(text="Save", command=save)
add_button.grid(column=2, row=4)

window.mainloop()
