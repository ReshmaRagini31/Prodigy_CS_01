import tkinter as tk
from tkinter import messagebox

def caesar_encrypt(plaintext, shift):
    """Encrypt the plaintext using Caesar cipher with the given shift."""
    encrypted_text = []
    
    for char in plaintext:
        if char.isalpha():  # Check if character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around using modulo 26
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)  # Non-alphabetic characters remain unchanged

    return ''.join(encrypted_text)

def caesar_decrypt(ciphertext, shift):
    """Decrypt the ciphertext using Caesar cipher with the given shift."""
    return caesar_encrypt(ciphertext, -shift)  # Decrypting is the same as encrypting with negative shift

def process_text():
    """Process the text based on user input."""
    action = action_var.get()
    shift_value = shift_entry.get()
    message = input_text.get("1.0", tk.END).strip()

    try:
        shift = int(shift_value)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer for the shift value.")
        return

    if action == 'Encrypt':
        result = caesar_encrypt(message, shift)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Encrypted Message: {result}")
    elif action == 'Decrypt':
        result = caesar_decrypt(message, shift)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Decrypted Message: {result}")

# Setting up the GUI
root = tk.Tk()
root.title("Caesar Cipher")

# Action selection
action_var = tk.StringVar(value='Encrypt')
encrypt_radio = tk.Radiobutton(root, text="Encrypt", variable=action_var, value='Encrypt')
decrypt_radio = tk.Radiobutton(root, text="Decrypt", variable=action_var, value='Decrypt')
encrypt_radio.pack()
decrypt_radio.pack()

# Shift value input
shift_label = tk.Label(root, text="Enter Shift Value:")
shift_label.pack()
shift_entry = tk.Entry(root)
shift_entry.pack()

# Input text area
input_label = tk.Label(root, text="Enter your message:")
input_label.pack()
input_text = tk.Text(root, height=10, width=50)
input_text.pack()

# Process button
process_button = tk.Button(root, text="Process", command=process_text)
process_button.pack()

# Output text area
output_label = tk.Label(root, text="Output:")
output_label.pack()
output_text = tk.Text(root, height=10, width=50)
output_text.pack()

# Run the application
root.mainloop()
