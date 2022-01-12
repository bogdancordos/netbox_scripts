import requests
import json
from extras.scripts import *

class RunCommand(Script):
    class Meta:
        name = "Lookup public IP for Domain details"
        description = "Lookup public IP for Domain details"
        field_order = ['input_ip']

    input_ip = StringVar(
        description="Lookup IP"
    )


    def run(self, data, commit):

        url = "http://ipwhois.app/json/%s" % data['input_ip']

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        rawoutput = response.text
        output = json.loads(rawoutput)
        
#
#Available fields:ip,success,type,continent,continent_code,country,country_code,country_flag,country_capital,country_phone,country_neighbours,
#                 region,city,latitude,longitude,asn,org,isp,timezone,timezone_name,timezone_dstOffset,timezone_gmtOffset,timezone_gmt,currency
#                 currency_code,currency_symbol,currency_rates,currency_plural,completed_requests
        
        self.log_success(f"IP :" + output['ip'])
        self.log_success(f"Type :" + output['type'])
        self.log_success(f"Continent :" + output['continent'])
        self.log_success(f"Country :" + output['country'])
        self.log_success(f"Region :" + output['region'])
        self.log_success(f"City :" + output['city'])
        self.log_success(f"ASN :" + output['asn'])
        self.log_success(f"Org :" + output['org'])
        self.log_success(f"ISP :" + output['isp'])
        self.log_success(f"Timezone :" + output['timezone'])

        #Requests tracking as unpaid version allow 10,000 requests per month
        return(output['completed_requests'])
