from abc import ABC, abstractmethod


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
