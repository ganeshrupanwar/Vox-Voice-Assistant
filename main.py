import sys
import time
from vad_detector import VAD
from recognizer import Recognizer
from tts import speak
import commands

# Wake-words
HOTWORDS = ["hey vox", "hello vox", "hi vox", "hey"]

# Map spoken phrases → (function, response-text)
CMD_MAP = {
    "open youtube":    (commands.open_youtube,    "Opening YouTube"),
    "open chrome":     (commands.open_chrome,     "Opening Chrome"),
    "open vscode":     (commands.open_vscode,     "Opening VS Code"),
    "open folder":     (commands.open_folder,     "Opening folder"),
    "search web":      (lambda: commands.search_web(last_query), "Searching the web"),
    "play music":      (commands.play_music,      "Playing music"),
    "what time":       (commands.tell_time,       "Telling the time"),
    "what date":       (commands.tell_date,       "Telling today’s date"),
    "shutdown":        (commands.shutdown_system, "Shutting down"),
    "restart":         (commands.restart_system,  "Restarting"),
    "lock screen":     (commands.lock_screen,     "Locking screen"),
    "volume up":       (commands.volume_up,       "Increasing volume"),
    "volume down":     (commands.volume_down,     "Decreasing volume"),
    "mute":            (commands.mute_volume,     "Muting volume"),
    "unmute":          (commands.unmute_volume,   "Unmuting volume"),
    "screenshot":      (commands.take_screenshot, "Taking screenshot"),
    "tell me a joke":  (commands.tell_joke,       "Here’s a joke"),
    "open email":      (commands.open_email,      "Opening email client"),
    "close window":    (commands.close_window,    "Closing window"),
    "open calculator": (commands.open_calculator, "Opening calculator"),
}

def main():
    vad        = VAD()
    recognizer = Recognizer()
    speak("Vox is online")

    global last_query
    last_query = ""

    while True:
        print("…listening…")
        audio = vad.listen_for_speech()
        text  = recognizer.recognize(audio).lower().strip()
        print("Heard:", text)

        if not text:
            time.sleep(0.2)
            continue

        executed = False

        # 1) Hot-word path
        for h in HOTWORDS:
            if h in text:
                cmd_text = text.split(h, 1)[1].strip()

                if cmd_text.startswith("search web"):
                    last_query = cmd_text.replace("search web", "").strip()

                for phrase, (func, resp) in CMD_MAP.items():
                    if phrase in cmd_text:
                        speak(resp)
                        func()
                        # if user asked to lock screen, exit immediately
                        if phrase == "lock screen":
                            sys.exit(0)
                        executed = True
                        break
                if not executed:
                    speak("Sorry, I didn’t catch that command.")
                break

        # 2) Fallback: direct commands (no wake-word)
        if not executed:
            for phrase, (func, resp) in CMD_MAP.items():
                if text.startswith(phrase):
                    speak(resp)
                    func()
                    # exit on lock screen here as well
                    if phrase == "lock screen":
                        sys.exit(0)
                    executed = True
                    break

        time.sleep(0.2)

if __name__ == "__main__":
    main()
