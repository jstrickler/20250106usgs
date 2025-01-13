from pprint import pprint
from erosapi.dataset import EROSDataset
from erosapi.scene import EROSScene

def main():
    # IRL, do NOT hard-code sensitive info in scripts!
    # Get from file, keyboard, or environment
    USERNAME = "jstrickler@gmail.com"
    TOKEN = "OFn!BsIVaWjZs!YqFRsH2WsXxP11WD0AIWXyYGGtDcG4EF0IM1F!WVoV3kPPH908"
    ds: EROSDataset = EROSDataset(username=USERNAME, application_token=TOKEN)
    print(f"{ds.username = }")
    print(f"{ds.application_token = }")
    print(f"{ds.login_token = }")
    catalogs = ds.get_catalog()
    print(f"{catalogs = }")
    parameters = {
        "datasetName": "Global Land Survey",
        "spatialFilter": {
            "filterType": "mbr",
            "lowerLeft": {
                    "latitude": 44.60847,
                    "longitude": -99.69639
            },
            "upperRight": {
                    "latitude": 44.60847,
                    "longitude": -99.69639
            }
        },
        "temporalFilter": {
            "start": "2012-01-01",
            "end": "2012-12-01"
        }
    }
    results = ds.search(params=parameters)
    pprint(results)

    print('-' * 60)
    
    sc = EROSScene(username=USERNAME, application_token=TOKEN)
    print(f"{sc = }")

    

if __name__ == "__main__":
    main()