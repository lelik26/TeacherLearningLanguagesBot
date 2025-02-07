from elevenlabs import save
from elevenlabs.client import ElevenLabs

import config as cfg

client = ElevenLabs(api_key=cfg.ELEVENLABS_API_KEY)

def get_all_voices():
    """Получает список доступных голосов"""
    voices = client.voices.get_all()
    return [{'name': voice.name, 'id': voice.voice_id} for voice in voices.voices]

def generate_audio(text: str, voice_id: str):
    """Генерирует аудиофайл"""
    audio = client.generate(text=text, voice=voice_id, model="eleven_multilingual_v2")
    filename = "audio.mp3"
    save(audio, filename)
    return filename



