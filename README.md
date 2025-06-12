# Vox Voice Assistant

Vox Voice Assistant is a Python‐based, desktop voice assistant for Windows. It listens for a wake word (“hey vox”, “hello vox”, “hi vox”), recognizes your spoken commands, and performs actions like opening applications, controlling volume, taking screenshots, and more just like Siri, Google Assistant, or Alexa.

## Overview

Vox uses `webrtcvad` for voice activity detection (VAD), the `SpeechRecognition` library for converting speech to text, and `pyttsx3` for text-to-speech. A `commands.py` module maps 20 basic voice commands (e.g., “open YouTube”, “volume up”, “tell me a joke”) to Python functions that execute the corresponding action.

## Features

- **Hot-word Activation**: “hey vox”, “hello vox”, “hi vox”.  
- **Voice Activity Detection**: Only captures speech segments with `webrtcvad`.  
- **Speech Recognition**: Google Speech API via `SpeechRecognition`.  
- **Natural Responses**: Announces actions in “-ing” form (“Opening Chrome”, “Taking screenshot”).  
- **20 Built-In Actions**: “open YouTube”, “volume up”, “tell me a joke” 
- **System Volume Control** via `pycaw`.  
- **Extensible**: Add new commands in `commands.py` and register in `CMD_MAP`.

## Technology Stack

- **Python 3.8+**  
- **webrtcvad** for VAD  
- **PyAudio** for microphone I/O  
- **SpeechRecognition** (Google API)  
- **pyttsx3** for offline TTS  
- **pycaw** & **comtypes** for Windows volume control  
- **Pillow** for screenshots

## Getting Started

To get started with this project, follow these instructions:

### Cloning the Repository

To clone the repository, run the following command:

```bash
git clone https://github.com/PrathameshBamb/Vox-Voice-Assistant.git
cd path to your project file
python main.py
```

