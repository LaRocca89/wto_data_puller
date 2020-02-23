from time_series_datapoints import *
from wto_api_key import *

get_time_series_datapoints('TP_A_0030', api_key) #outputs a JSON file with the desired indicator
get_time_series_datapoints('TP_A_0030', api_key, frmt='csv') #outputs a csv file with the desired indicator
