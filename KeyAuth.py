import time
from pynput import keyboard

def on_press(key):
    try:
        # Record the time when a key is pressed
        key_press_times.append(time.time())
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop the listener when the 'esc' key is pressed
        return False

def calculate_dwell_times(key_press_times):
    # Calculate the time interval between consecutive key presses (dwell time)
    dwell_times = []
    for i in range(1, len(key_press_times)):
        dwell_time = key_press_times[i] - key_press_times[i - 1]
        dwell_times.append(dwell_time)
    return dwell_times

def main():
    global key_press_times
    key_press_times = []

    # Collect keystroke data until the 'esc' key is pressed
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        print("Collecting keystroke data. Press 'esc' to stop.")
        listener.join()

    # Calculate dwell times between consecutive key presses
    dwell_times = calculate_dwell_times(key_press_times)

    # Print the dwell times for demonstration purposes
    print("Dwell times:")
    for time_interval in dwell_times:
        print(time_interval)

if __name__ == "__main__":
    main()
