import tkinter as tk
import os

# Block function
def block_website():
    website = website_entry.get()
    with open("C:\Windows\System32\drivers\etc\hosts", "r+") as file:
        content = file.read()
        if website in content:
            status_label.config(text="Website is already blocked!")
            website_entry.delete(0, tk.END)
            return
        else:
            file.write("127.0.0.1 " + website + "\n")
            status_label.config(text="Website blocked successfully!")
            website_entry.delete(0, tk.END)
            
# UnBlock function
def unblock_website():
    website = website_entry.get()
    with open("C:\Windows\System32\drivers\etc\hosts", "r+") as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not website in line:
                file.write(line)
        file.truncate()
        status_label.config(text="Website unblocked successfully!")
        website_entry.delete(0, tk.END)

root = tk.Tk()
root.geometry("500x400")  # window size
root.title("Website Blocker")

#  website entry field
website_entry = tk.Entry(root, width=40, font=("Arial", 16))
website_entry.pack(pady=20)

#  block button
block_button = tk.Button(root, text="Block Website", command=block_website, font=("Arial", 16))
block_button.pack(pady=10)

#  unblock button
unblock_button = tk.Button(root, text="Unblock Website", command=unblock_website, font=("Arial", 16))
unblock_button.pack(pady=10)

# Create status label
status_label = tk.Label(root, text="", font=("Arial", 16))
status_label.pack(pady=20)

root.mainloop()
