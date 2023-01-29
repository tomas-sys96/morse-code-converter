import subprocess

from message_converter import MessageConverter, TextConverter, MorseCodeConverter


logo = """
╔═╗╔═╗                   ╔═══╗      ╔╗        ╔═══╗                    ╔╗        
║║╚╝║║                   ║╔═╗║      ║║        ║╔═╗║                   ╔╝╚╗       
║╔╗╔╗║╔══╗╔═╗╔══╗╔══╗    ║║ ╚╝╔══╗╔═╝║╔══╗    ║║ ╚╝╔══╗╔═╗ ╔╗╔╗╔══╗╔═╗╚╗╔╝╔══╗╔═╗
║║║║║║║╔╗║║╔╝║══╣║╔╗║    ║║ ╔╗║╔╗║║╔╗║║╔╗║    ║║ ╔╗║╔╗║║╔╗╗║╚╝║║╔╗║║╔╝ ║║ ║╔╗║║╔╝
║║║║║║║╚╝║║║ ╠══║║║═╣    ║╚═╝║║╚╝║║╚╝║║║═╣    ║╚═╝║║╚╝║║║║║╚╗╔╝║║═╣║║  ║╚╗║║═╣║║ 
╚╝╚╝╚╝╚══╝╚╝ ╚══╝╚══╝    ╚═══╝╚══╝╚══╝╚══╝    ╚═══╝╚══╝╚╝╚╝ ╚╝ ╚══╝╚╝  ╚═╝╚══╝╚╝ 
"""

alphabet = {
        "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..",
        "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
        "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."
    }


def main(alphabet: dict):
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


if __name__ == "__main__":
    main(alphabet)
