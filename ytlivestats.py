import json
import threading
from urllib.request import urlopen

import time


class YTLiveStats:

    ytapikey = None
    workers = {}

    def __init__(self, apikey):
        self.ytapikey = apikey

    def build_apiurl(self, stream_id):
        return 'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics%2CliveStreamingDetails&id=' + stream_id + '&key=' + self.ytapikey

    def get_livedata(self, stream_id):
        if not self.ytapikey:
            raise ValueError('The youtube API key was not set.')
        if not stream_id:
            raise ValueError('The stream id was not set.')
        return json.loads(urlopen(self.build_apiurl(stream_id)).read())

    def start_DataLoop(self, delay, stream_id, callback_updated):
        cached_id = threading.get_ident()
        self.workers[str(cached_id)] = True
        while self.workers[str(cached_id)]:
            data = self.get_livedata(stream_id)
            callback_updated(data)
            time.sleep(delay)

    def end_recording(self, ident):
        if str(ident) in self.workers:
            self.workers[str(ident)] = False

    def record_data(self, delay, data_receiver, stream_id):
        recorder_thread = threading.Thread(target=self.start_DataLoop, args=(delay, stream_id, data_receiver))
        recorder_thread.start()
        return recorder_thread.ident

    def set_apikey(self, apikey):
        self.ytapikey = apikey
