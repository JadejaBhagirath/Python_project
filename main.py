#Morse code Translator:
#Convert text to Morse code and vice versa.
#play the morse code through sound (beeps) or 

# Dictionary for morese code
# Morse Code dictionary mapping letters and numbers to Morse code
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.',
    
    ' ': '/'  # Space between words in Morse code
}
# Basic code function.

def encode_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        else:
            morse_code += '? '  # Placeholder for unknown characters
    return morse_code.strip()


#Decoding Function: Write a function to decode Morse code back to text.

def decode_from_morse(morse):
    morse_to_text = {value: key for key, value in morse_code_dict.items()}
    words = morse.split(' / ')
    decoded_message = ''
    for word in words:
        for code in word.split():
            if code in morse_to_text:
                decoded_message += morse_to_text[code]
            else:
                decoded_message += '?'  # Placeholder for unknown sequences
        decoded_message += ' '
    return decoded_message.strip()

#Create a Simple Interface: Allow the user to choose between encoding and decoding.

def main():
    choice = input("Type '1' to Encode to Morse, '2' to Decode from Morse: ")
    
    if choice == '1':
        text = input("Enter the text to encode: ")
        encoded = encode_to_morse(text)
        print("Encoded Morse Code:", encoded)
    
    elif choice == '2':
        morse = input("Enter the Morse code to decode (use '/' for spaces between words): ")
        decoded = decode_from_morse(morse)
        print("Decoded Text:", decoded)
    
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

