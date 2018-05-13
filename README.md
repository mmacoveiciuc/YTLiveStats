YTLiveStats
=====
---
YTLiveStats is a simple way to retrieve live streaming data asynchronously with callback functions. Very simple to use, and currently very limited. You will be able to start a recording which calls back to your function of choice every given time interval to provide you all data about the live stream.

This data is **NOT** scraped, it requires that you have a [YouTube data v3 api key](https://developers.google.com/youtube/v3/getting-started).

Also take note that the YouTube data api has quotas for api usage. If you use over 1,000,000 points (a unit they use to determine how expensive a request/operation is), your ability to access the api will be throttled. This should not be an issue for most people, you will be able to make thousands of regular size requests without the need to worry about the limit.

See more at [Google Developer Console](https://console.developers.google.com)

#### How do I use it?

Clone the project and follow the example written. The same example will be provided on here for convenience.

The stream id can be found by accessing a stream on YouTube and copying the id from the URL, it should look something like this: https://www.youtube.com/watch?v=xxxxxxxxxx
Copy the part of the URL indicated by the x's and you've gotten the live stream id!

```Python
from threading import Timer

from ytlivestats import YTLiveStats # import the module

# Our callback function, in this case it simply prints the data.
# Access the data as a Python dict.
def my_data_receiver(data):
    print(data)

#Initialize the api with your api key
api = YTLiveStats('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

# Start a recording of the live stream, returns the thread id.
#   paramter_1: the time interval at which to get the data
#   parameter_2: the callback function
#   parameter_3: the stream id
thread_id = api.record_data(5, my_data_receiver, 'qeHQfaS3z8E')

# Ends the recording!
def end_stream():
	api.end_recording(thread_id)

t = Timer(20, end_stream) # After 20 seconds call the end stream function
t.start() # Start the timer
```
