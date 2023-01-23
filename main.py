from abc import ABC, abstractmethod
import subprocess


logo = """
╔═╗╔═╗                   ╔═══╗      ╔╗        ╔═══╗                    ╔╗        
║║╚╝║║                   ║╔═╗║      ║║        ║╔═╗║                   ╔╝╚╗       
║╔╗╔╗║╔══╗╔═╗╔══╗╔══╗    ║║ ╚╝╔══╗╔═╝║╔══╗    ║║ ╚╝╔══╗╔═╗ ╔╗╔╗╔══╗╔═╗╚╗╔╝╔══╗╔═╗
║║║║║║║╔╗║║╔╝║══╣║╔╗║    ║║ ╔╗║╔╗║║╔╗║║╔╗║    ║║ ╔╗║╔╗║║╔╗╗║╚╝║║╔╗║║╔╝ ║║ ║╔╗║║╔╝
║║║║║║║╚╝║║║ ╠══║║║═╣    ║╚═╝║║╚╝║║╚╝║║║═╣    ║╚═╝║║╚╝║║║║║╚╗╔╝║║═╣║║  ║╚╗║║═╣║║ 
╚╝╚╝╚╝╚══╝╚╝ ╚══╝╚══╝    ╚═══╝╚══╝╚══╝╚══╝    ╚═══╝╚══╝╚╝╚╝ ╚╝ ╚══╝╚╝  ╚═╝╚══╝╚╝ 
"""


class MessageConverter(ABC):
    def __init__(self, morse_code_alphabet: dict):
        self.morse_code_alphabet = morse_code_alphabet
        self.letter_separator: str = 3 * " "
        self.word_separator: str = 7 * " "
        self.invalid_characters: int = 0

    @abstractmethod
    def convert_message(self, message) -> str:
        pass

    @abstractmethod
    def _convert_word(self, word) -> str:
        pass

    @abstractmethod
    def _convert_letter(self, letter, letter_index):
        pass


class TextConverter(MessageConverter):

    def convert_message(self, message: str) -> str:
        converted_message = ""
        words = message.split()
        for word_index, word in enumerate(words):
            # Check if it's the first word in the message
            # In case it isn't, add a word separator
            if word_index != 0:
                converted_message += self.word_separator
            converted_word = self._convert_word(word)
            converted_message += converted_word
        converted_message = converted_message.strip()
        return converted_message

    def _convert_word(self, word: str) -> str:
        converted_word = ""
        for letter_index, letter in enumerate(word):
            converted_letter = self._convert_letter(letter, letter_index)
            if converted_letter:
                converted_word += converted_letter
            else:
                self.invalid_characters += 1
        return converted_word

    def _convert_letter(self, letter: str, letter_index: int):
        # Check if it's the first letter in a word
        # In case it isn't, add a letter separator
        if letter in self.morse_code_alphabet and letter_index != 0:
            return self.letter_separator + self.morse_code_alphabet[letter]
        elif letter in self.morse_code_alphabet:
            return self.morse_code_alphabet[letter]
        else:
            return None


class MorseCodeConverter(MessageConverter):

    def convert_message(self, message: str) -> str:
        converted_message = ""
        morse_words = message.split(sep=self.word_separator)
        for morse_word_index, morse_word in enumerate(morse_words):
            morse_letters = morse_word.split(sep=self.letter_separator)
            # Don't add a blank space if it's the first word in the message
            if morse_word_index != 0:
                converted_message += " "
            converted_word = self._convert_word(morse_letters)
            converted_message += converted_word
        return converted_message

    def _convert_word(self, word: list) -> str:
        converted_word = ""
        for morse_letter in word:
            converted_letter = self._convert_letter(morse_letter, 0)
            if converted_letter:
                converted_word += converted_letter
            else:
                self.invalid_characters += 1
        return converted_word

    def _convert_letter(self, letter: str, letter_index: int):
        morse_symbols = list(self.morse_code_alphabet.values())
        if letter in morse_symbols:
            position = morse_symbols.index(letter)
            alphabet_letters = list(self.morse_code_alphabet.keys())
            return alphabet_letters[position]
        else:
            return None


def show_rules():
    print(logo)
    print("""Rules of conversion:
    1. The length of a dot is one unit.
    2. The space between letters is three units.
    3. The space between words is seven units.""")
    print("\n(Hint: Use . as dits and - as dahs.)")


def select_conversion() -> str:
    while True:
        conversion = input("\nType 't' to convert text to Morse code, or\n"
                           "type 'm' to convert Morse code to text:\n").lower()
        if conversion == "t" or conversion == "m":
            return conversion


def read_message() -> str:
    message = input(f"\nMessage to convert:\n").lower()
    return message


def show_converted_messaged(message: str, message_converter: MessageConverter):
    if message_converter.invalid_characters > 0:
        print(f"\nConverted message ({message_converter.invalid_characters} invalid characters skipped):\n"
              f"{message}")
    else:
        print(f"\nConverted message:\n{message}")


def convert_again():
    keep_converting = input("\nType 'y' if you wish to convert another message,\n"
                            "otherwise press any other button to exit:\n").lower()
    if keep_converting == "y":
        return True
    else:
        return False


def clear_console():
    subprocess.run("cls", shell=True)


alphabet = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..",
    "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
    "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."
}

if __name__ == "__main__":
    while True:
        show_rules()
        selected_conversion = select_conversion()
        entered_message = read_message()

        if selected_conversion == "t":
            converter = TextConverter(alphabet)
            message_after_conversion = converter.convert_message(entered_message)
        else:
            converter = MorseCodeConverter(alphabet)
            message_after_conversion = converter.convert_message(entered_message)

        show_converted_messaged(message_after_conversion, converter)

        if convert_again():
            clear_console()
        else:
            break
