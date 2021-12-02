#add netmiko to the local_requirements.txt
from django.utils.text import slugify
from netmiko import ConnectHandler
import netbox.settings
from extras.scripts import *


class RunCommand(Script):
    class Meta:
        name = "Run command on Cisco Devices via SSH"
        description = "Run command on Cisco Devices via SSH"
        field_order = ['input_ip', 'input_command']


    input_ip = StringVar(
        description="Enter the IP Address:"
    )
    input_command = StringVar(
        description="Enter the SSH command:"
    )

    def run(self, data, commit):

        cisco1 = { 
            "device_type": "cisco_ios",
            "host": data['input_ip'],
            "username": netbox.settings.NAPALM_USERNAME,
            "password": netbox.settings.NAPALM_PASSWORD,
        }

        command = data['input_command']

        with ConnectHandler(**cisco1) as net_connect:
            output = net_connect.send_command(command)

            self.log_success(output)
        return "Success"
