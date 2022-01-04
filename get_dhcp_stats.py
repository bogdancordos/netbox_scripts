from netmiko import ConnectHandler
from django.utils.text import slugify
import netbox.settings
from dcim.models import Device
from ipam.models import IPAddress
from dcim.choices import DeviceStatusChoices
from extras.scripts import *
from netaddr import *


class RunCommand(Script):
    class Meta:
        name = "View DHCP Stats"
        description = "View DHCP Stats on Cisco DHCP Servers"
        field_order = ['select_device','input_command']


    select_device = ObjectVar(
        description="Select the device:",
        model = Device,
        default = None,
        required = True,
        query_params = {
             'has_primary_ip' : 'True'}
    )


    CHOICES = (
        ('show ip dhcp pool | i .', 'Show DHCP Pools'),
        ('show ip dhcp binding', 'Show DHCP Bindings')
    )
    input_command = ChoiceVar(
        choices=CHOICES
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

        command = data['input_command']

        with ConnectHandler(**cisco1) as net_connect:
            output = net_connect.send_command(command)


            self.log_success("View the information bellow")
        return '' .join(output)
