#pip install librosa

import librosa
import numpy as np

def calcular_bpm_promedio(ruta_archivo):
    # Cargar el archivo de audio WAV
    y, sr = librosa.load(ruta_archivo)

    # Calcular el tempo (BPM) del archivo de audio
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    tempo, _ = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)

    return tempo

if __name__ == "__main__":
    # Ejemplo de uso
    ruta_archivo_wav = "archivo_audio.wav"  # Ruta al archivo de audio WAV
    bpm_promedio = calcular_bpm_promedio(ruta_archivo_wav)
    print(f"BPM promedio del archivo de audio: {bpm_promedio}")