import tkinter as tk
from tkinter import messagebox

def encrypted(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def process_message():
    shift_value = shift_entry.get()
    if not shift_value.isdigit():
        messagebox.showerror("Error", "Shift value must be an integer.")
        shift_entry.delete(0, tk.END)  # Clear the entry field
        return

    shift = int(shift_value)
    message_type = message_type_var.get()
    message = message_entry.get()

    if message_type == 1:
        encrypted_message = encrypted(message, shift)
        messagebox.showinfo("Encrypted Message", f"Encrypted message: {encrypted_message}")
    else:
        decrypted_message = decrypt(message, shift)
        messagebox.showinfo("Decrypted Message", f"Decrypted message: {decrypted_message}")

    # Clear entry fields
    message_entry.delete(0, tk.END)
    shift_entry.delete(0, tk.END)

    # Set focus on message entry field
    message_entry.focus_set()

# Create main window
root = tk.Tk()
root.title("Caesar Cipher")
root.resizable(True, True)

# Message type
message_type_var = tk.IntVar()
tk.Label(root, text="Message type:").grid(row=0, column=0, sticky="w")
tk.Radiobutton(root, text="Encrypt", variable=message_type_var, value=1).grid(row=0, column=1, sticky="w")
tk.Radiobutton(root, text="Decrypt", variable=message_type_var, value=2).grid(row=0, column=2, sticky="w")

# Message
tk.Label(root, text="Message:").grid(row=1, column=0, sticky="w")
message_entry = tk.Entry(root)
message_entry.grid(row=1, column=1, columnspan=2)
message_entry.focus_set()  # Set focus on message entry field by default

# Shift
tk.Label(root, text="Shift value:").grid(row=2, column=0, sticky="w")
shift_entry = tk.Entry(root)
shift_entry.grid(row=2, column=1, columnspan=2)

# Bind "Tab" key to move between entry fields
message_entry.bind("<Tab>", lambda e: shift_entry.focus_set())
shift_entry.bind("<Tab>", lambda e: message_entry.focus_set())

# Process button
process_button = tk.Button(root, text="Process", command=process_message)
process_button.grid(row=3, column=1)

root.mainloop()
