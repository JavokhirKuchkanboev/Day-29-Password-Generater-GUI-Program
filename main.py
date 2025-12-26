from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    all_chars = letters + numbers + symbols
    password = ''.join(random.choice(all_chars) for _ in range(12))
    pyperclip.copy(password)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

    window.clipboard_clear()
    window.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops",
            message="Please make sure you haven't left any fields empty."
        )
        return   # 👈 STOP the function here

    is_ok = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered:\n"
                f"Email: {email}\n"
                f"Password: {password}\n"
                f"Is it ok to save?"
    )

    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    



# ---------------------------- WINDOW ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=40)

# ---------------------------- CANVAS (LOGO) ------------------------------- #
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3, pady=(0, 25))

# ---------------------------- GRID CONFIG (NEW) ------------------------------- #
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=3)
window.grid_columnconfigure(2, weight=2)

# ---------------------------- LABELS ------------------------------- #
website_label = Label(text="Website")
website_label.grid(column=0, row=1, sticky="E", pady=4)

email_label = Label(text="Email / Username")
email_label.grid(column=0, row=2, sticky="E", pady=4)

password_label = Label(text="Password")
password_label.grid(column=0, row=3, sticky="E", pady=4)

# ---------------------------- ENTRIES ------------------------------- #
website_entry = Entry(width=32)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW", pady=4)
website_entry.focus()

email_entry = Entry(width=32)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW", pady=4)
email_entry.insert(0, "example@email.com")

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3, sticky="EW", pady=4)

# ---------------------------- BUTTONS ------------------------------- #
generate_button = Button(text="Generate", width=12, command=generate_password)
generate_button.grid(column=2, row=3, padx=(8, 0), pady=4)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, pady=(18, 0), sticky="EW")

window.mainloop()
