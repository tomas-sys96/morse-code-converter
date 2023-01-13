from ascii_art import logo


class MorseConverter:

    def __init__(self):
        self.morse_dict = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--.."
        }
        self.letter_sep = 3 * " "
        self.word_sep = 7 * " "
        self.converted_message = None

    def text_to_morse(self, text):
        morse_code = ""
        words = text.split()
        for word in words:
            for letter in word:
                # Skip unknown characters
                try:
                    morse_code += self.morse_dict[letter]
                except KeyError:
                    pass
                # Don't add a letter separator if it is the last letter in a word
                if letter != word[-1]:
                    morse_code += self.letter_sep
            # Don't add a word separator if it is the last word
            if word != words[-1]:
                morse_code += self.word_sep
        return morse_code

    def morse_to_text(self, morse_code):
        text = ""
        words = morse_code.split(sep=self.word_sep)
        for word in words:
            letters = word.split(sep=self.letter_sep)
            for letter in letters:
                # Loop through the dictionary and search for corresponding letters
                for key, value in self.morse_dict.items():
                    if value == letter:
                        text += key
            # Add a blank space at the end of each word
            text += " "
        return text

    def execute_conversion(self):
        converted_message = None
        not_selected = True
        while not_selected:
            selected_operation = input("\nType 't' to convert text to Morse code, or\n"
                                       "type 'm' to convert Morse code to text:\n").lower()
            if selected_operation == "t":
                not_selected = False
                message = input(f"\nText to Morse code:\n").lower()
                converted_message = self.text_to_morse(text=message)
            elif selected_operation == "m":
                not_selected = False
                message = input(f"\nMorse code to text:\n").lower()
                converted_message = self.morse_to_text(morse_code=message)
            else:
                pass
        return converted_message


morse_converter = MorseConverter()

continue_converting = True
while continue_converting:
    # Display logo and rules of conversion
    print(logo)
    print("""Rules of conversion:
            1. The length of a dot is one unit.
            2. The space between letters is three units.
            3. The space between words is seven units.""")
    print("\n(Hint: Use . as dits and - as dahs.)")

    # Get converted message
    converted_msg = morse_converter.execute_conversion()
    print(f"\nConverted message:\n{converted_msg}")

    # Ask the user if they want to continue
    want_to_continue = input("\nType 'n' if you want to exit, otherwise press any other button to continue:\n").lower()
    if want_to_continue == "n":
        continue_converting = False
    else:
        pass
