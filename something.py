import tkinter as tk
from tkinter import messagebox

def validate_login():
    global logged_in_user, main_frame
    username = username_entry.get()
    password = password_entry.get()

    # Check if username and password are correct (you can replace this with your validation logic)
    if username == "admin" and password == "admin":
        logged_in_user = username  # Store logged-in user
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        login_frame.pack_forget()  # Hide login frame
        main_frame.pack()  # Show main frame
        logged_in_label.config(text=f"Logged in as: {username}")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def logout():
    global logged_in_user
    logged_in_user = None
    messagebox.showinfo("Logged Out", "You have been logged out")
    main_frame.pack_forget()  # Hide main frame
    login_frame.pack()  # Show login frame

# Create main window
root = tk.Tk()
root.title("Login Page")

# Set window dimensions to 340x585
window_width = 340  # Width in pixels
window_height = 585  # Height in pixels
root.geometry(f"{window_width}x{window_height}")

# Create frames
login_frame = tk.Frame(root)
main_frame = tk.Frame(root)

# Username label and entry
username_label = tk.Label(login_frame, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1, padx=10, pady=5)

# Password label and entry
password_label = tk.Label(login_frame, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Login button
login_button = tk.Button(login_frame, text="Login", command=validate_login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Logout button
logout_button = tk.Button(main_frame, text="Logout", command=logout)
logout_button.pack(pady=10)

# Label to display logged-in user
logged_in_label = tk.Label(main_frame, text="")
logged_in_label.pack()

# Hide main frame initially
main_frame.pack_forget()

# Global variable to store logged-in user
logged_in_user = None

# Pack login frame initially
login_frame.pack()

# Run the main loop
root.mainloop()
