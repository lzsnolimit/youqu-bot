import os
import uuid

import edge_playback
import edge_tts

from common import log
from config import azure_conf


async def edge_tss(TEXT):
    file_path = os.path.join(azure_conf("temp_file_path"), uuid.uuid1().hex + ".mp3")
    voice = azure_conf("voice_name")
    log.info("TTS start! text:{} voice:{}", TEXT, voice)
    tts = edge_tts.Communicate(text=TEXT, voice=voice)
    log.info("TTS finished! path:{}", file_path)

#    tts.save(file_path)
    #await tts.save(file_path)
