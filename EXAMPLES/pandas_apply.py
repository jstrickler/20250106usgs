import time
import requests
import pandas as pd

URL_BASE = "http://api.macvendors.com/"




def main():
    df_list = pd.read_html('http://192.168.1.254/cgi-bin/home.ha', match="Roku")
    print(f"len(df_list): {len(df_list)}")

    home_devices = df_list.pop()

    # home_devices = pd.read_csv('../DATA/ClientList.csv')

    # home_devices['Manufacturer'] = home_devices.apply(get_mfr_by_mac, axis=1)
    print(home_devices.info())
    print()
    #
    print(home_devices[['Client Name', 'Client IP address', 'Manufacturer']])
    print()
    print(home_devices.iloc[-1])

def get_mfr_by_mac(row):
    mac = row['Clients MAC Address']
    url = URL_BASE + mac
    response = requests.get(url)
    if response.status_code == requests.codes.OK:
        mfr = response.text
    else:
        mfr = 'UNKNOWN'
    time.sleep(1.1)  # don't over-request from API
    return f"{mfr}"


if __name__ == '__main__':
    main()
