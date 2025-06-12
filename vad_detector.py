import webrtcvad, pyaudio, speech_recognition as sr

class VAD:
    def __init__(self, aggressiveness=3):
        self.rate = 16000
        self.frame_ms = 30
        self.frame_samples = int(self.rate * self.frame_ms / 1000)
        self.frame_bytes   = self.frame_samples * 2

        self.vad = webrtcvad.Vad(aggressiveness)
        pa = pyaudio.PyAudio()
        self.stream = pa.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.frame_samples
        )

        # after speech starts, stop when you see this many silence frames in a row
        self.max_silence_frames = 15   # ~15 * 30ms = 450ms
        # never record for more than ~5 seconds
        self.max_frames = int((5 * 1000) / self.frame_ms)

    def listen_for_speech(self):
        frames = []
        triggered = False
        silence_count = 0
        total_frames = 0

        while True:
            chunk = self.stream.read(self.frame_samples, exception_on_overflow=False)
            if len(chunk) != self.frame_bytes:
                continue

            is_speech = self.vad.is_speech(chunk, self.rate)

            if not triggered:
                if is_speech:
                    triggered = True
                    frames.append(chunk)
            else:
                frames.append(chunk)
                total_frames += 1
                if not is_speech:
                    silence_count += 1
                else:
                    silence_count = 0

                if silence_count > self.max_silence_frames or total_frames > self.max_frames:
                    break

        return sr.AudioData(b"".join(frames), self.rate, 2)
