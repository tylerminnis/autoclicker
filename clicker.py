import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

#controls
delay = 0.0001
button = Button.left
start_stop_key = KeyCode(char = 'a')
stop_key = KeyCode(char = 'c')

class ClickMouse(threading.Thread):

    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    #doesn't work for some reason
    def start_clicking(self):
        self.running = True

    #doesn't work for some reason
    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
        time.sleep(0.1)

mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
            print('Stopped running!')
        else:
            click_thread.start_clicking()
            print('Started running!')
    elif key == stop_key:
        click_thread.exit()        
        listener.stop()
        print('Exited program!')

with Listener(on_press=on_press) as listener:
    listener.join()
