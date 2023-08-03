import asyncio

from common import log
import config
from common.tss import edge_tss
from speech_sample import speech_recognize_keyword_locally_from_microphone, speech_recognize_async_from_file, \
    speech_recognize_once_from_mic

if __name__ == '__main__':
    try:
        # load config
        config.load_config()
        query=speech_recognize_keyword_locally_from_microphone()
        asyncio.run(edge_tss(query))
    except Exception as e:
        log.error("App startup failed!")
        log.exception(e)