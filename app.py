from common import log
import config
from speech_sample import speech_recognize_keyword_locally_from_microphone, speech_recognize_async_from_file

if __name__ == '__main__':
    try:
        # load config
        config.load_config()
        speech_recognize_keyword_locally_from_microphone()
        speech_recognize_async_from_file("AudioFromRecognizedKeyword.wav")
    except Exception as e:
        log.error("App startup failed!")
        log.exception(e)