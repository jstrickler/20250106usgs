from typing import Any
import json
from erosapi.erosbase import EROSBase

class EROSDataset(EROSBase):
    # def __init__(self):
    #     super().__init__()
    #     # local code

    def get_catalog(self):
        return self._get_data(endpoint="dataset-catalogs", params={})
    
    def search(self, *, params: dict[str,Any]):
        return self._get_data(
            endpoint="dataset-search",
            params=params,
        )
