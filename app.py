import asyncio

from common import log
import config
from service.socket_connection import socket_handler
from service.tss import edge_tss
from speech_sample import speech_recognize_keyword_locally_from_microphone

if __name__ == '__main__':
    try:
        # load config
        config.load_config()
        socketio = socket_handler()
        socketio.send_heartbeat()
        # query=speech_recognize_keyword_locally_from_microphone()
        # asyncio.run(edge_tss(query))
    except Exception as e:
        log.error("App startup failed!")
        log.exception(e)