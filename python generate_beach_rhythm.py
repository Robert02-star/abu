from pydub import AudioSegment
from pydub.generators import Sine
import simpleaudio as sa

# Crear una onda sinusoidal para el ritmo
def generate_beat(frequency, duration, volume=-10.0):
    return Sine(frequency).to_audio_segment(duration=duration).apply_gain(volume)

# Duraciones en milisegundos
beat_duration = 300  # Duración de cada golpe
pause_duration = 150  # Duración de la pausa entre golpes

# Crear los golpes del ritmo
kick = generate_beat(60, beat_duration)
snare = generate_beat(200, beat_duration)
hi_hat = generate_beat(400, beat_duration)

# Crear una pausa
pause = AudioSegment.silent(duration=pause_duration)

# Crear un patrón de ritmo playero
pattern = (
    kick + pause + snare + pause +
    hi_hat + pause + snare + pause +
    kick + pause + snare + pause +
    hi_hat + pause + hi_hat + pause
)

# Repetir el patrón para hacer una pista más larga
rhythm = pattern * 4

# Exportar el ritmo a un archivo de audio
rhythm.export("beach_rhythm.wav", format="wav")

# Reproducir el archivo de audio
wave_obj = sa.WaveObject.from_wave_file("beach_rhythm.wav")
play_obj = wave_obj.play()
play_obj.wait_done()
