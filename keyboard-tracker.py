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
        
print("Press keys (Press ESC to stop)\n")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
