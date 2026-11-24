from pynput import keyboard
import tkinter as tk
import threading

locked = False
listener = None

def on_press(key):
    # Keep suppressing keyboard input while locked.
    if locked:
        return False

def lock_keyboard():
    global locked, listener

    if locked:
        return 

    locked = True

    listener = keyboard.Listener(
        on_press=on_press,
        suppress=True
    )

    listener.start()
    status.config(text="Keyboard Locked")

def unlock_keyboard():
    global locked, listener

    locked = False

    if listener:
        listener.stop()
        listener = None

    status.config(text="Keyboard Unlocked")

root = tk.Tk()
root.title("Keyboard Lock")
root.geometry("320x200")

status = tk.Label(
    root,
    text="Keyboard Unlocked",
    font=("Arial", 14)
)
status.pack(pady=20)

tk.Button(
    root,
    text="Lock Keyboard",
    command=lock_keyboard
).pack(pady=10)

tk.Button(
    root,
    text="Unlock Keyboard",
    command=unlock_keyboard
).pack(pady=10)

root.mainloop()
