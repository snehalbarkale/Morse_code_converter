# Title
logo = r"""
  _____        _     _         __  __                    ___         _        ___                     _           
 |_   _|____ _| |_  | |_ ___  |  \/  |___ _ _ ___ ___   / __|___  __| |___   / __|___ _ ___ _____ _ _| |_ ___ _ _ 
   | |/ -_) \ /  _| |  _/ _ \ | |\/| / _ \ '_(_-</ -_) | (__/ _ \/ _` / -_) | (__/ _ \ ' \ V / -_) '_|  _/ -_) '_|
   |_|\___/_\_\\__|  \__\___/ |_|  |_\___/_| /__/\___|  \___\___/\__,_\___|  \___\___/_||_\_/\___|_|  \__\___|_|                                                                                                                                                                                                           
"""
print(logo)
# Morse Code Dictionary
TEXT_TO_MORSE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': '/'  # Space between words
}

# Morse → Text dictionary
MORSE_TO_TEXT = {v: k for k, v in TEXT_TO_MORSE.items()}


# Function to convert text to Morse
def text_to_morse(text):
    text = text.upper()
    morse_code = ''
    for char in text:
        if char in TEXT_TO_MORSE:
            morse_code += TEXT_TO_MORSE[char] + ' '
        else:
            print(f"Warning: Character '{char}' is not supported. Only letters A-Z, numbers 0-9, and space are allowed.")
            morse_code += ' Invalid '
    return morse_code.strip()


# Function to convert Morse to text
def morse_to_text(morse):
    words = morse.strip().split(' / ')  # Slash for space between words
    decoded_text = ''
    for word in words:
        for code in word.split():
            decoded_text += MORSE_TO_TEXT.get(code, '?')
        decoded_text += ' '
    return decoded_text.strip()

while True:
    print("\n--- Morse Code Converter ---")
    print("1. Text to Morse Code")
    print("2. Morse Code to Text")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        text = input("Enter text to convert to Morse: ")
        result = text_to_morse(text)
        print("Morse Code:", result)

    elif choice == '2':
        print("Enter Morse code using '.' and '-' with '/' for space")
        morse = input("Enter Morse code: ")
        result = morse_to_text(morse)
        print("Text:", result)

    elif choice == '3':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
