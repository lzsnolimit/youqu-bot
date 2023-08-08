import config
from common import log
from service.azure_speech_service import speech_recognize_keyword_locally_from_microphone

from service.socket_connection import init_sio

if __name__ == '__main__':
    try:
        # load config
        config.load_config()
        init_sio()

        while True:
            log.info("start to listen")
            speech_recognize_keyword_locally_from_microphone()




# asyncio.run(edge_tss(query))
    except Exception as e:
        log.error("App startup failed!")
        log.exception(e)
