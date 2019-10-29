from time import sleep
import keyboard

sleep(5)
for i in range(300):
    keyboard.press("space")
##    keyboard.call_later(lambda a=0: keyboard.release("a"), args=("a"), delay=0.1)
##sleep(2)
    sleep(0.01)
    keyboard.release("space")

##sleep(5)
##keyboard.press("a")
##sleep(3)
##keyboard.release("a")
##print("finished")

##keyboard.press_and_release('shift+s, space')

##keyboard.write('The quick brown fox jumps over the lazy dog.')

##keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))

# Press PAGE UP then PAGE DOWN to type "foobar".
##keyboard.add_hotkey('page up, page down', lambda: keyboard.write('foobar'))

# Blocks until you press esc.
##keyboard.wait('esc')

# Record events until 'esc' is pressed.
##recorded = keyboard.record(until='esc')
# Then replay back at three times the speed.
##keyboard.play(recorded, speed_factor=3)

# Type @@ then press space to replace with abbreviation.
##keyboard.add_abbreviation('@@', 'my.long.email@example.com')

# Block forever, like `while True`.
##keyboard.wait()






##from pynput.keyboard import Key, Controller
##
##keyboard = Controller()
##
##sleep(3)
##
##keyboard.press('a')
##sleep(10)
##keyboard.release('a')
##
##print("finished")
