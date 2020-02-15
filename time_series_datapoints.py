"""Developed by Greg LaRocca, Please send any questions or comments to larocca89@gmail.com
This project is incomplete and will be refined over time."""
import requests
import json
"""
This script creates a simple defined function that can pull times series data from the WTO's API. 
For more information on the WTO's api see: https://apiportal.wto.org/
Special thank you to the Requests library's team of developers for making this possible.
"""


# for information on parameters see:
# https://apiportal.wto.org/docs/services/version1/operations/get-data-i-i
def get_time_series_datapoints(indicator_code,   # strings only
                               key,     # strings only
                               filename,    # strings only
                               reporting_economy='all',
                               partner_economy='default',
                               time_period='default',
                               product_sector='default',
                               product_sub_sector='false',
                               frmt='json',  # CSV files are possible... I need an If-Else loop here
                               output_mode='full',
                               decimals='default',
                               offset=0,  # number of records to skip
                               max_records=500,  # maximum number of records
                               heading_style='H',
                               language=1,  # 1 = English; 2 = French; 3 = Spanish
                               metadata='false'
                               ):
    endpoint = f"https://api.wto.org/timeseries/v1/data?i={indicator_code}&r={reporting_economy}" \
               f"&p={partner_economy}&ps={time_period}&pc={product_sector}&spc={product_sub_sector}&fmt={frmt}" \
               f"&mode={output_mode}&dec={decimals}&off={offset}&max={max_records}" \
               f"&head={heading_style}&lang={language}" \
               f"&meta={metadata}&subscription-key={key}"
    response = requests.get(endpoint)
    assert response.status_code == 200, "Oh snap, this didn't work"
    json_data = response.json()
    with open(filename+'.json', 'w') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)
