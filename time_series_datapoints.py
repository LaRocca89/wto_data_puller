"""
Developed by Greg LaRocca, Please send any questions or comments to larocca89@gmail.com
This project is version complete. However, the library will be refined over time as new features are requested.
This script creates a simple defined function that can pull times series data from the WTO's API.
For more information on the WTO's api see: https://apiportal.wto.org/
Special thank you to the Requests library's team of developers for making this possible.
"""
import requests
import json
import io
import zipfile
import time


# for information on parameters see:
# https://apiportal.wto.org/docs/services/version1/operations/get-data-i-i
def get_json_data(url,
                  proxies=None):
    response = requests.get(url, proxies=proxies)
    assert response.status_code == 200, "There was an error in the request"
    json_data = response.json()
    with open('WTO_API_TimeseriesData_' + str(time.strftime('%Y%m%d%H%M%S')) + '.json', 'w') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)


def get_csv_data(url,
                 proxies=None):
    r = requests.get(url, proxies=proxies)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()


def get_time_series_datapoints(indicator_code,  # strings only
                               key,  # strings only
                               reporting_economy='all',
                               partner_economy='default',
                               time_period='default',
                               product_sector='default',
                               product_sub_sector='false',
                               frmt='json',
                               output_mode='full',
                               decimals='default',
                               offset=0,  # number of records to skip
                               max_records=500,  # maximum number of records
                               heading_style='H',
                               language=1,  # 1 = English; 2 = French; 3 = Spanish
                               metadata='false',
                               proxies=None
                               ):
    endpoint = f"https://api.wto.org/timeseries/v1/data?i={indicator_code}&r={reporting_economy}" \
               f"&p={partner_economy}&ps={time_period}&pc={product_sector}&spc={product_sub_sector}&fmt={frmt}" \
               f"&mode={output_mode}&dec={decimals}&off={offset}&max={max_records}" \
               f"&head={heading_style}&lang={language}" \
               f"&meta={metadata}&subscription-key={key}"
    if frmt == 'json':
        response = requests.get(endpoint, proxies=proxies)
        assert response.status_code == 200, "There was an error in the request"
        json_data = response.json()
        with open('WTO_API_TimeseriesData_' + str(time.strftime('%Y%m%d%H%M%S')) + '.json', 'w') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
    elif frmt == 'csv':
        r = requests.get(endpoint, proxies=proxies)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall()
    else:
        print('File format is invalid')


# API only outputs JSON files for get_time_series_data_count data
def get_time_series_data_count(indicator_code,
                               key,
                               reporting_economy='all',
                               partner_economy='default',
                               time_period='default',
                               product_sector='default',
                               product_sub_sector='false',
                               proxies=None
                               ):
    endpoint = f"https://api.wto.org/timeseries/v1/data_count?i={indicator_code}&r={reporting_economy}" \
               f"&p={partner_economy}&ps={time_period}&pc={product_sector}" \
               f"&spc={product_sub_sector}&subscription-key={key}"
    response = requests.get(endpoint, proxies=proxies)
    json_data = response.json()
    with open('WTO_API_TimeseriesDataCount_' + str(time.strftime('%Y%m%d%H%M%S')) + '.json', 'w') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)


def get_time_series_metadata(indicator_code,
                             key,
                             reporting_economy='all',
                             partner_economy='all',
                             product_sector='all',
                             product_sub_sector='false',
                             lang=1,
                             proxies=None
                             ):
    endpoint = f'https://api.wto.org/timeseries/v1/metadata?i={indicator_code}&r={reporting_economy}' \
               f'&p={partner_economy}&pc={product_sector}&spc={product_sub_sector}&lang={lang}&subscription-key={key}'
    response = requests.get(endpoint, proxies=proxies)
    json_data = response.json()
    with open('WTO_API_TimeseriesMetadata_' + str(time.strftime('%Y%m%d%H%M%S')) + '.json', 'w') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)


def get_topics(
        key,
        lang=1,
        proxies=None):
    endpoint = f'https://api.wto.org/timeseries/v1/topics?lang={lang}&subscription-key={key}'
    response = requests.get(endpoint, proxies=proxies)
    json_data = response.json()
    with open('WTO_API_TimeseriesTopics_' + str(time.strftime('%Y%m%d%H%M%S')) + '.json', 'w') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)


def get_frequencies(key,
                    lang=1,
                    proxies=None):
    endpoint = f'https://api.wto.org/timeseries/v1/frequencies?lang={lang}&subscription-key={key}'
    response = requests.get(endpoint, proxies=proxies)
    json_data = response.json()
    with open('WTO_API_TimeseriesFrequencies_' + str(time.strftime('%Y%m%d%H%M%S')) + '.json', 'w') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)


def get_periods(key,
                lang=1,
                proxies=None):
    endpoint = f'https://api.wto.org/timeseries/v1/periods?lang={lang}&subscription-key={key}'
    response = requests.get(endpoint, proxies=proxies)
    json_data = response.json()
    with open('WTO_API_TimeseriesPeriods_' + str(time.strftime('%Y%m%d%H%M%S')) + '.json', 'w') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)


def get_units(key,
              lang=1,
              proxies=None):
    endpoint = f'https://api.wto.org/timeseries/v1/units?lang={lang}&subscription-key={key}'
    response = requests.get(endpoint, proxies=proxies)
    json_data = response.json()
    with open('WTO_API_TimeseriesUnits_' + str(time.strftime('%Y%m%d%H%M%S')) + '.json', 'w') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)


def get_indicator_categories(key,
                             lang=1,
                             proxies=None):
    endpoint = f'https://api.wto.org/timeseries/v1/indicator_categories?lang={lang}&subscription-key={key}'
    response = requests.get(endpoint, proxies=proxies)
    json_data = response.json()
    with open('WTO_API_TimeseriesIndicatorCategories_' + str(time.strftime('%Y%m%d%H%M%S')) + '.json', 'w') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)


def get_indicators(key,
                   indicator_code='all',
                   name=None,
                   topics='all',
                   product_classification='all',
                   trade_partner='all',
                   frequency='all',
                   lang=1,
                   proxies=None):
    if name is None:
        endpoint = f'https://api.wto.org/timeseries/v1/indicators?i={indicator_code}&t={topics}' \
                   f'&pc={product_classification}&tp={trade_partner}&frq={frequency}&lang={lang}' \
                   f'&subscription-key={key}'
        response = requests.get(endpoint, proxies=proxies)
        assert response.status_code == 200, "There was an error in the request"
        json_data = response.json()
        with open('WTO_API_TimeseriesIndicator_' + str(time.strftime('%Y%m%d%H%M%S')) + '.json', 'w') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
    else:
        endpoint = f'https://api.wto.org/timeseries/v1/indicators?i={indicator_code}&name={name}&t={topics}' \
                   f'&pc={product_classification}&tp={trade_partner}&frq={frequency}&lang={lang}' \
                   f'&subscription-key={key}'
        response = requests.get(endpoint, proxies=proxies)
        assert response.status_code == 200, "There was an error in the request"
        json_data = response.json()
        with open('WTO_API_TimeseriesIndicator_' + str(time.strftime('%Y%m%d%H%M%S')) + '.json', 'w') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)


def get_regions(key,
                lang=1,
                proxies=None):
    endpoint = f'https://api.wto.org/timeseries/v1/territory/regions?lang={lang}&subscription-key={key}'
    response = requests.get(endpoint, proxies=proxies)
    assert response.status_code == 200, "There was an error in the request"
    json_data = response.json()
    with open('WTO_API_TimeseriesRegions_' + str(time.strftime('%Y%m%d%H%M%S')) + '.json', 'w') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)


def get_economic_groups(key,
                        lang=1,
                        proxies=None):
    endpoint = f'https://api.wto.org/timeseries/v1/territory/groups?lang={lang}&subscription-key={key}'
    response = requests.get(endpoint, proxies=proxies)
    assert response.status_code == 200, "There was an error in the request"
    json_data = response.json()
    with open('WTO_API_TimeseriesEconomicGroups_' + str(time.strftime('%Y%m%d%H%M%S')) + '.json', 'w') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)


def get_reporting_economies(key,
                            name=None,
                            economy='all',
                            region='all',
                            group='all',
                            lang=1,
                            proxies=None):
    if name is None:
        endpoint = f'https://api.wto.org/timeseries/v1/reporters?ig={economy}&reg={region}&gp={group}' \
                   f'&lang={lang}&subscription-key={key}'
        response = requests.get(endpoint, proxies=proxies)
        assert response.status_code == 200, "There was an error in the request"
        json_data = response.json()
        with open('WTO_API_TimeseriesReportingEconomies_' + str(time.strftime('%Y%m%d%H%M%S')) + '.json', 'w') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
    else:
        endpoint = f'https://api.wto.org/timeseries/v1/reporters?name={name}&ig={economy}&reg={region}&gp={group}' \
                   f'&lang={lang}&subscription-key={key}'
        response = requests.get(endpoint, proxies=proxies)
        assert response.status_code == 200, "There was an error in the request"
        json_data = response.json()
        with open('WTO_API_TimeseriesReportingEconomies_' + str(time.strftime('%Y%m%d%H%M%S')) + '.json', 'w') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)


def get_partner_economies(key,
                          name=None,
                          economy='all',
                          region='all',
                          group='all',
                          lang=1,
                          proxies=None):
    if name is None:
        endpoint = f'https://api.wto.org/timeseries/v1/partners?ig={economy}&reg={region}&gp={group}' \
                   f'&lang={lang}&subscription-key={key}'
        response = requests.get(endpoint, proxies=proxies)
        assert response.status_code == 200, "There was an error in the request"
        json_data = response.json()
        with open('WTO_API_TimeseriesPartnerEconomies_' + str(time.strftime('%Y%m%d%H%M%S')) + '.json', 'w') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
    else:
        endpoint = f'https://api.wto.org/timeseries/v1/partners?name={name}&ig={economy}&reg={region}&gp={group}' \
                   f'&lang={lang}&subscription-key={key}'
        response = requests.get(endpoint, proxies=proxies)
        assert response.status_code == 200, "There was an error in the request"
        json_data = response.json()
        with open('WTO_API_TimeseriesPartnerEconomies_' + str(time.strftime('%Y%m%d%H%M%S')) + '.json', 'w') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)


def get_classifications(key,
                        lang=1,
                        proxies=None):
    endpoint = f'https://api.wto.org/timeseries/v1/product_classifications?lang={lang}&subscription-key={key}'
    response = requests.get(endpoint, proxies=proxies)
    assert response.status_code == 200, "There was an error in the request"
    json_data = response.json()
    with open('WTO_API_TimeseriesProductClassifications_' + str(time.strftime('%Y%m%d%H%M%S')) + '.json', 'w') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)


def get_products(key,
                 name=None,
                 product_classification='all',
                 lang=1,
                 proxies=None):
    if name is None:
        endpoint = f'https://api.wto.org/timeseries/v1/products?pc={product_classification}&lang={lang}' \
                     f'&subscription-key={key}'
        response = requests.get(endpoint, proxies=proxies)
        assert response.status_code == 200, "There was an error in the request"
        json_data = response.json()
        with open('WTO_API_TimeseriesProducts&Sectors_' + str(time.strftime('%Y%m%d%H%M%S')) + '.json', 'w') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
    else:
        endpoint = f'https://api.wto.org/timeseries/v1/products?name={name}&pc={product_classification}' \
                   f'&lang={lang}&subscription-key={key}'
        response = requests.get(endpoint, proxies=proxies)
        assert response.status_code == 200, "There was an error in the request"
        json_data = response.json()
        with open('WTO_API_TimeseriesProducts&Sectors_' + str(time.strftime('%Y%m%d%H%M%S')) + '.json', 'w') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)


def get_years(key,
              proxies=None):
    endpoint = f'https://api.wto.org/timeseries/v1/years?subscription-key={key}'
    response = requests.get(endpoint, proxies=proxies)
    assert response.status_code == 200, "There was an error in the request"
    json_data = response.json()
    with open('WTO_API_TimeseriesYears_' + str(time.strftime('%Y%m%d%H%M%S')) + '.json', 'w') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)


def get_value_flags(key,
                    lang=1,
                    proxies=None):
    endpoint = f'https://api.wto.org/timeseries/v1/value_flags?lang={lang}&subscription-key={key}'
    response = requests.get(endpoint, proxies=proxies)
    assert response.status_code == 200, "There was an error in the request"
    json_data = response.json()
    with open('WTO_API_TimeseriesValueFlags_' + str(time.strftime('%Y%m%d%H%M%S')) + '.json', 'w') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)
