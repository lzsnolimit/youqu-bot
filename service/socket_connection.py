import socketio

from common import log
from config import socket_conf

sio = socketio.Client(reconnection=True, reconnection_attempts=5, reconnection_delay=5, reconnection_delay_max=60,
                      request_timeout=1000)


def init_sio():
    #if sio is not connected, connect it
    if not sio.connected:
        path = '{}?token={}'.format(socket_conf('wsurl'), socket_conf('token'))
        log.info(path)
        sio.connect(path, transports='websocket', namespaces=['/chat'])


def register_socketio_events(self, event, callback, namespace='/chat'):
    self.sio.on(event, callback, namespace=namespace)


def send_heartbeat():
    sio.emit('heartbeat', "ping", namespace='/chat')


@sio.on('message', namespace='/chat')
def on_message(data):
    log.info('I received a message!{}', data)


@sio.on('heartbeat', namespace='/chat')
def on_heartbeat(data):
    log.info('I received a heartbeat!{}', data)


@sio.on('connected', namespace='/chat')
def connect(self):
    log.info("I'm connected!")
