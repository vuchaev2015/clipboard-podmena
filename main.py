import pyperclip
from pynput import keyboard

print('Starting to read the clipboard')

russian_letters = ['у', 'Е', 'е', 'Н', 'Х', 'х', 'В', 'А', 'а', 'Р', 'р', 'О', 'о', 'С', 'с', 'М', 'Т']
english_letters = ['y', 'E', 'e', 'H', 'X', 'x', 'B', 'A', 'a', 'P', 'p', 'O', 'o', 'C', 'c', 'M', 'T']

def on_release(key):
    if key == keyboard.Key.esc:
        return False

while True:
    with keyboard.Listener(
                on_release=on_release) as listener:
                listener.join()

    clipboard = pyperclip.paste()
    output = ''

    for i, s in enumerate(clipboard, 1):
        if s in russian_letters:
            output += english_letters[russian_letters.index(s)]
        else:
            if s in english_letters:
                output += russian_letters[english_letters.index(s)]
            else:
                output += s


    if not output == clipboard:
        print('The letters on the clipboard have been replaced')
        pyperclip.copy(output)

    else:
        print('Could not find similar letters to replace')
        pass
            
