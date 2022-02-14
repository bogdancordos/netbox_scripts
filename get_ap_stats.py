from netmiko import ConnectHandler
from django.utils.text import slugify
import netbox.settings
from dcim.models import Device, DeviceRole
from ipam.models import IPAddress
from extras.scripts import *
from netaddr import *


class RunCommand(Script):
    class Meta:
        name = "View AP Associated Clients"
        description = "View AP Associated Clients"
        field_order = ['role', 'select_device']

    role = ObjectVar(
        model = DeviceRole,
        query_params={
            'name' : 'Wireless AP'
        }
    )

    select_device = ObjectVar(
        description="Select an AP:",
        model = Device,
        default = None,
        required = True,
        query_params = {
            'role_id' : '$role'
        }
    )
    def run(self, data, commit):

        address = data['select_device'].primary_ip
        input_ip = str(address.address.ip)

        cisco1 = {
            "device_type": "cisco_ios",
            "host": input_ip,
            "username": netbox.settings.NAPALM_USERNAME,
            "password": netbox.settings.NAPALM_PASSWORD,
        }

        command = "show dot11 associations client"

        with ConnectHandler(**cisco1) as net_connect:
            output = net_connect.send_command(command)


            self.log_success("View the information bellow")
        return '' .join(output)
