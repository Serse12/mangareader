from actions.button_functions import prev_page, next_page, zoom_in, zoom_out

from pynput import keyboard
import threading

# Define the key combinations
def on_press(key):
    try:
        if key == keyboard.Key.left:
            prev_page()
        elif key == keyboard.Key.right:
            next_page()
        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            print("Ctrl key pressed")
    except AttributeError:
        pass

def on_release(key):
    try:
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            print("Ctrl key released")
        elif key == keyboard.KeyCode.from_char('+'):
            zoom_in()
        elif key == keyboard.KeyCode.from_char('-'):
            zoom_out()
        if key == keyboard.Key.esc:
            # Stop the listener when the Escape key is pressed
            return False
    except AttributeError:
        pass

def start_listener():
    # Start the listener in a separate thread
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

def run_keyboard():
    # Start listener in a separate thread
    listener_thread = threading.Thread(target=start_listener)
    listener_thread.start()
