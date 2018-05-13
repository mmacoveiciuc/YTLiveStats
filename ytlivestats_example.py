from threading import Timer

from ytlivestats import YTLiveStats


def my_data_receiver(data):
    print(data)


api = YTLiveStats('API KEY')
thread_id = api.record_data(5, my_data_receiver, 'qeHQfaS3z8E')

t = Timer(60, api.end_recording(thread_id))
t.start()
