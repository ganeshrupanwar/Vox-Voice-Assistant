import os
import platform
import subprocess
import webbrowser
import time
from PIL import ImageGrab

# ---- pycaw imports for volume control ----
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# get the system audio endpoint
_devices = AudioUtilities.GetSpeakers()
_interface = _devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
_volume = cast(_interface, POINTER(IAudioEndpointVolume))


def open_youtube():
    try:
        subprocess.Popen(["chrome", "https://www.youtube.com"])
    except Exception:
        webbrowser.open("https://www.youtube.com")


def open_chrome():
    try:
        subprocess.Popen(["chrome"])
    except Exception:
        webbrowser.open("https://www.google.com")


def open_vscode():
    try:
        subprocess.Popen(["code", "."])
    except Exception as e:
        print("VS Code not found:", e)


def open_folder(path=r"D:\Music"):
    if os.path.isdir(path):
        os.startfile(path)
    else:
        print("Folder not found:", path)


def search_web(query):
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(url)


def play_music(music_folder=r"D:\Music"):
    open_folder(music_folder)


def tell_time():
    print(time.strftime("Current time is %I:%M %p"))


def tell_date():
    print(time.strftime("Today's date is %B %d, %Y"))


def shutdown_system():
    if platform.system() == "Windows":
        os.system("shutdown /s /t 1")
    elif platform.system() == "Linux":
        os.system("shutdown now")
    else:
        os.system("sudo shutdown -h now")


def restart_system():
    if platform.system() == "Windows":
        os.system("shutdown /r /t 1")
    elif platform.system() == "Linux":
        os.system("reboot")
    else:
        os.system("sudo reboot")


def lock_screen():
    if platform.system() == "Windows":
        os.system("rundll32.exe user32.dll,LockWorkStation")


# ---- real volume control via pycaw ----

def volume_up(delta: float = 0.05):
    """Increase volume by delta (default 5%)."""
    current = _volume.GetMasterVolumeLevelScalar()
    new = min(current + delta, 1.0)
    _volume.SetMasterVolumeLevelScalar(new, None)
    print(f"Volume increased to {int(new * 100)}%")

def volume_down(delta: float = 0.05):
    """Decrease volume by delta (default 5%)."""
    current = _volume.GetMasterVolumeLevelScalar()
    new = max(current - delta, 0.0)
    _volume.SetMasterVolumeLevelScalar(new, None)
    print(f"Volume decreased to {int(new * 100)}%")

def mute_volume():
    _volume.SetMute(1, None)
    print("Muted")

def unmute_volume():
    _volume.SetMute(0, None)
    print("Unmuted")


def take_screenshot(save_path="screenshot.png"):
    img = ImageGrab.grab()
    img.save(save_path)
    print("Screenshot saved to", save_path)


def tell_joke():
    print("Why did the programmer quit his job? Because he didn’t get arrays.")


def open_email():
    if platform.system() == "Windows":
        os.system("start outlookmail:")
    else:
        webbrowser.open("mailto:")


def close_window():
    # you can implement with pyautogui if you like
    print("Close window (not implemented)")


def open_calculator():
    if platform.system() == "Windows":
        os.system("calc")
    elif platform.system() == "Linux":
        subprocess.Popen(["gnome-calculator"])
    else:
        print("Calculator launch not supported on this OS.")
