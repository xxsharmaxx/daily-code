from pynput import keyboard

def on_press(key):
    try:
        print(f"Key pressed: {key.char}")
    except AttributeError:
        print(f"Special key pressed: {key}")
def on_release(key):
    if key == keyboard.Key.esc:
        print("\nExiting program...")
        return False
        
