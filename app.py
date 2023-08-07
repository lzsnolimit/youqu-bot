from common import log
import config
from service.azure_speech_service import speech_recognize_keyword_locally_from_microphone
from service.socket_connection import init_sio, send_message

if __name__ == '__main__':
    try:
        # load config
        config.load_config()
        init_sio()

        while True:
            log.info("start to listen")
            query = speech_recognize_keyword_locally_from_microphone()




    # asyncio.run(edge_tss(query))
    except Exception as e:
        log.error("App startup failed!")
        log.exception(e)
