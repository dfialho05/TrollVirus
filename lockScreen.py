from ctypes import windll

def lock_screen():
    windll.user32.LockWorkStation()

lock_screen()