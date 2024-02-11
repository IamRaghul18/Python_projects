import tkinter as tk

def copy_to_clipboard(text):
    root.clipboard_clear()
    root.clipboard_append(text)

def copy_morse():
    morse_code = morse_result_label.cget("text").split(": ")[1]
    copy_to_clipboard(morse_code)

def copy_english():
    english_text = english_result_label.cget("text").split(": ")[1]
    copy_to_clipboard(english_text)



english_to_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.'
}

# Reverse the mapping for Morse to English
morse_to_english = {value: key for key, value in english_to_morse.items()}

def convert_to_morse():
    english_text = english_entry.get().upper()
    morse_result = ''
    for char in english_text:
        if char == ' ':  # Change space in English to '/' in Morse code
            morse_result += '/ '
        elif char in english_to_morse:
            morse_result += english_to_morse[char] + ' '
        else:
            morse_result += char + ' '    # If the character is not found in the dictionary, add as is

    morse_result_label.config(text=f"Morse code: {morse_result}")

def convert_to_english():
    morse_code = morse_entry.get().split(' ')  # Split Morse code by space to get individual codes
    english_result = ''
    for code in morse_code:
        if code == '/':  # Change '/' in Morse code to space in English
            english_result += ' '
        elif code in morse_to_english:
            english_result += morse_to_english[code]
        else:
            english_result += code
    english_result_label.config(text=f"Translated text: {english_result}")


# Create the main window
root = tk.Tk()
root.title("Morse Code Translator")

# English to Morse code section
english_label = tk.Label(root, text="Enter English text:")
english_label.pack()

english_entry = tk.Entry(root)
english_entry.pack()

english_entry.focus()
english_entry.bind('<Return>', lambda event: convert_to_morse())

morse_result_label = tk.Label(root, text="Morse code: ..........")
morse_result_label.pack()


# Morse code to English section
morse_label = tk.Label(root, text="Enter Morse code:")
morse_label.pack()

morse_entry = tk.Entry(root)
morse_entry.pack()

morse_entry.bind('<Return>', lambda event: convert_to_english())


english_result_label = tk.Label(root, text="Translated text: ..........")
english_result_label.pack()

# Copy buttons for translated text and Morse code

morse_button = tk.Button(root, text="Copy Morse", command=copy_morse)
morse_button.pack()

english_button = tk.Button(root, text="Copy English", command=copy_english)
english_button.pack()

trans_label = tk.Label(root, text="Click Enter for translation")
trans_label.pack()
copied_label = tk.Label(root, text="Click buttons to copy")
copied_label.pack()
root.mainloop()