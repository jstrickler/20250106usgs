import time
import requests
import pandas as pd

MAC_VENDOR_URL_TEMPLATE = "http://api.macvendors.com/{}"

ROUTER_URL_1 = 'http://192.168.1.254/cgi-bin/home.ha'
ROUTER_MATCH_1 = "Roku"
DEVICE_LIST_1_DROP_LIST = ['Device IP Address / Name', ]

ROUTER_URL_2 = 'http://192.168.1.254/cgi-bin/lanstatistics.ha'
ROUTER_MATCH_2 = "Authentication"

def main():
    # create the first dataframe from one page
    df_list = pd.read_html(ROUTER_URL_1, match=ROUTER_MATCH_1)
    device_list_1 = df_list.pop()
    device_list_1[['IP', 'Name']] = device_list_1['Device IP Address / Name'].str.split(' / ', expand=True)
    device_list_1.drop(DEVICE_LIST_1_DROP_LIST, axis=1, inplace=True)
    print(f"device_list_1.info(): {device_list_1.info()}")
    print('-' * 60)
    print(device_list_1.head())

    # create the second dataframe from a different page
    df_list = pd.read_html(ROUTER_URL_2, match=ROUTER_MATCH_2)
    device_list_2 = df_list.pop()
    print(f"device_list_2.info(): {device_list_2.info()}")
    print('-' * 60)
    print(device_list_2.head())

    merged_list = pd.merge(device_list_1, device_list_2, left_on="IP", right_on="IP Address")

    print(merged_list.shape)
    print('-' * 60)
    print(merged_list.info())
    print('-' * 60)
    print(merged_list.head())
    print('-' * 60)
    print(merged_list.iloc[0])
if __name__ == '__main__':
    main()
