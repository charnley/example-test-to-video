import wave
from piper import PiperVoice

def generate_audio(voice, text_script, audio_filename):

    audio_filename = audio_filename.with_suffix(".wav")

    with wave.open(str(audio_filename), "wb") as wav_file:
        voice.synthesize_wav(text_script, wav_file)

    return audio_filename

