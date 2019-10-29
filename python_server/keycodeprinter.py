import keyboard


def callback(event):
    print("Key Name Is {}, And Key Code Is {}".format(event.name, event.scan_code))

keyboard.hook(callback, suppress=False)
