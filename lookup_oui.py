import requests
import json
from extras.scripts import *

class RunCommand(Script):
    class Meta:
        name = "Lookup MAC"
        description = "Lookup MAC"
        field_order = ['input_data']

    input_data = StringVar(
        description="Lookup MAC"
    )


    def run(self, data, commit):
        mac = str(data['input_data'])
        url = "https://api.macvendors.com/%s"%(mac)

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        rawoutput = response.text


        self.log_success(f"Lookup Complete")

        return(rawoutput)
