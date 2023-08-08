import asyncio
import subprocess
import time
import uuid

import socketio

from common import log
from config import socket_conf
from service.azure_tts_service import AZURE


sio = socketio.Client(reconnection=True, reconnection_attempts=5, reconnection_delay=5, reconnection_delay_max=60,
                      request_timeout=1000)


def init_sio():
    # if sio is not connected, connect it
    if not sio.connected:
        path = '{}?token={}'.format(socket_conf('wsurl'), socket_conf('token'))
        log.info(path)
        sio.connect(path, transports=['websocket'], namespaces=['/chat'])
        log.info("sio connected")
    else:
        log.info("sio already connected")


def register_socketio_events(self, event, callback, namespace='/chat'):
    self.sio.on(event, callback, namespace=namespace)


def send_heartbeat():
    log.info("send heartbeat")
    try:
        sio.emit('heartbeat', "ping", namespace='/chat')
    except Exception as e:
        log.error("send heartbeat failed")

def send_heartbeat_job():
    while True:
        send_heartbeat()
        time.sleep(30)
        if not sio.connected:
            return
def send_message(query):
    if query is None:
        log.info("query is None")
        return False
    # if sio is not connected, connect it
    if not sio.connected:
        init_sio()
    log.info("send message {}", query)
    data = {'msg': query, 'messageID': uuid.uuid1().hex, 'response_type': 'text', 'model': socket_conf('model'),
            'conversation_id': subprocess.check_output("uuidgen").decode('utf-8').strip()}
    log.info("conversation_id:{}", socket_conf('conversation_id'))
    data['system_prompt'] = socket_conf('system_prompt')
    sio.emit('message', data, namespace='/chat')



def run_in_event_loop(coroutine):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(coroutine)

@sio.on('final', namespace='/chat')
def on_message(data):
    log.info('I received a message!{}', data)
    content = data['content']
    log.info("content:{}", content)
    if content is None:
        log.info("content is None")
        return False
    AZURE().synthesize_speech(content)



@sio.on('heartbeat', namespace='/chat')
def on_heartbeat(data):
    log.info('I received a heartbeat!{}', data)


@sio.event(namespace='/chat')
def connect():
    log.info("I'm connected!")
    #sio.start_background_task(send_heartbeat_job())


@sio.event(namespace='/chat')
def connect_error():
    log.info("The connection failed!")

@sio.event(namespace='/chat')
def disconnect():
    log.info("I'm disconnected!")


