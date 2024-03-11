#pip install youtube_dl moviepy

import youtube_dl
from moviepy.editor import *

def descargar_audio_desde_youtube(url, nombre_archivo):
    # Configuración de youtube_dl para descargar solo el audio
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',  # Cambiar a WAV
            'preferredquality': '192',
        }],
        'outtmpl': f'{nombre_archivo}.%(ext)s',  # Nombre del archivo de salida
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Se obtiene el nombre del archivo WAV generado
    nombre_archivo_wav = f"{nombre_archivo}.wav"

    return nombre_archivo_wav

if __name__ == "__main__":
    # Ejemplo de uso
    url_youtube = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Ejemplo de URL de YouTube
    nombre_archivo_salida = "audio_salida"

    archivo_wav = descargar_audio_desde_youtube(url_youtube, nombre_archivo_salida)
    print(f"El archivo WAV ha sido generado: {archivo_wav}")