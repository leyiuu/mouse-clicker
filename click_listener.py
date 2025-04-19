# ======================================
# click_listener.py
# Usage: python click_listener.py
# Listens for a single mouse click anywhere on screen and prints its coordinates.
# Requires: pip install pynput
# ======================================

from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Clicked at: (x={x}, y={y})")
        # Stop after first click
        return False

if __name__ == "__main__":
    print("Please click anywhere on the screen...")
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
