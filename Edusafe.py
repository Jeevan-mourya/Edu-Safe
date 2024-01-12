import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import platform
import os
import re
system = platform.system()
if system == "Windows":
    host_path = r'C:\Windows\System32\drivers\etc\hosts'
    ip_address = '127.0.0.1'
elif system == "Darwin":  # macOS
    host_path = '/private/etc/hosts'
    ip_address = '127.0.0.1'
elif system == "Linux":
    host_path = '/etc/hosts'
    ip_address = '127.0.0.1'
else:
    print("Unsupported operating system:", system)
    exit()
def save_user_details(username, email, password):
    directory = "user_details"
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, f"{username}.txt")
    with open(file_path, 'w') as f:
        f.write(f"Username: {username}\n")
        f.write(f"Email: {email}\n")
        f.write(f"Password: {password}\n"
def open_website_blocker(username, email, password):
    save_user_details(username, email, password)
    # Create the main window
    window = tk.Tk()
    window.title("Website Blocker")
    window.geometry("360x640")  # Mobile screen size
    # Load and display the background image
    background_image = Image.open("C:/Users/hp/Downloads/WhatsApp Image 2023-06-05 at 18.41.41.jpg")
    background_image = background_image.resize((360, 640), Image.ANTIALIAS)
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(window, image=background_photo)
    background_label.place(x=0, y=0)


    # Create the label and entry field
    label = tk.Label(window, text=" Enter Websites to Block/Unblock ", font=("Times", 14), fg="black", bg="MistyRose3")
    label.pack(pady=120)
    entry = tk.Entry(window, font=("Arial", 12))
    entry.pack(pady=0)
    def block_websites():
        websites = entry.get().strip().split(",")
        blocked = False
        with open(host_path, 'r+') as host_file:
            file_content = host_file.read()
            for web in websites:
                if web in file_content:
                    messagebox.showinfo("Website Blocker", "Already Blocked")
                    blocked = True
                    break
            if not blocked:
                for web in websites:
                    host_file.write(ip_address + " " + web.strip() + '\n')
                messagebox.showinfo("Website Blocker", "Blocked")
    def unblock_websites():
        websites = entry.get().strip().split(",")
        unblocked = False
        with open(host_path, 'r+') as host_file:
            file_content = host_file.readlines()
            host_file.seek(0)
            for line in file_content:
                if not any(web.strip() in line for web in websites):
                    host_file.write(line)
                else:
                    unblocked = True
            host_file.truncate()
        if unblocked:
            messagebox.showinfo("Website Blocker", "Unblocked")
        else:
            messagebox.showinfo("Website Blocker", "Already Unblocked")
    def update_blocked_websites():
        with open(host_path, 'r') as host_file:
            blocked_websites = [line.strip().split()[1] for line in host_file if line.strip().startswith(ip_address)]
            blocked_websites_text.set("\n".join(blocked_websites))
    def show_blocked_websites():
        update_blocked_websites()

    # Create the block and unblock buttons
    button_frame = tk.Frame(window, bg="grey")
    button_frame.pack(pady=5)
    block_button = tk.Button(button_frame, text="Block", font=("Arial", 12), command=block_websites, fg="gold",
                             bg="black")
    block_button.pack(side=tk.LEFT, padx=10)
    unblock_button = tk.Button(button_frame, text="Unblock", font=("Arial", 12), command=unblock_websites, fg="gold",
                               bg="black")
    unblock_button.pack(side=tk.LEFT)
    # Create the label to display blocked websites
    blocked_websites_label = tk.Label(window, text="Blocked Websites:", font=("Arial", 12), fg="gold", bg="blue")
    blocked_websites_label.pack(pady=10)
    blocked_websites_text = tk.StringVar()
    blocked_websites_text.set("")
    blocked_websites_display = tk.Label(window, textvariable=blocked_websites_text, font=("Arial", 12), fg="white",
                                        bg="grey", justify=tk.LEFT)
    blocked_websites_display.pack()



    # Create the button to show blocked websites
    blocked_button = tk.Button(window, text="Show Blocked Websites", font=("Arial", 12), command=show_blocked_websites,
                               fg="gold", bg="blue")
    blocked_button.pack(pady=10)
    # Start the main event loop
    window.mainloop()
def open_login_window():
    # Create the login window
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("360x640")  # Mobile screen size
    # Load and display the background image
    background_image = Image.open("C:/Users/hp/Downloads/—Pngtree—black gold fashion iphone8 mobile_1107853.jpg")
    background_image = background_image.resize((360, 640), Image.ANTIALIAS)
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(login_window, image=background_photo)
    background_label.place(x=0, y=0)
    # Create a label for the app name
    app_name_label = tk.Label(login_window, text="Edu-SAFE", font=("Arial", 20, "bold"), fg="black", bg="grey")
    app_name_label.pack(pady=30)

    # Create labels and entry fields for username, email, and password
    username_label = tk.Label(login_window, text="Username:", font=("Arial", 12), fg="black", bg="grey")
    username_label.pack(pady=15)
    username_entry = tk.Entry(login_window, font=("Arial", 12))
    username_entry.pack()
    email_label = tk.Label(login_window, text="Email:", font=("Arial", 12), fg="black", bg="grey")
    email_label.pack(pady=10)
    email_entry = tk.Entry(login_window, font=("Arial", 12))
    email_entry.pack()
    password_label = tk.Label(login_window, text="Password:", font=("Arial", 12), fg="black", bg="grey")
    password_label.pack(pady=10)
    password_entry = tk.Entry(login_window, show="*", font=("Arial", 12))
    password_entry.pack()
    def proceed_to_website_blocker():
        username = username_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        if username and email and password:
            login_window.destroy()
            open_website_blocker(username, email, password)
        else:
            messagebox.showinfo("Login", "Please fill in all fields.")
    # Create the login button
    login_button = tk.Button(login_window, text="Login", font=("Arial", 12), command=proceed_to_website_blocker,
                             fg="gold", bg="blue")
    login_button.pack(pady=20)
    # Start the main event loop
    login_window.mainloop()
# Start the application by opening the login window
open_login_window()
