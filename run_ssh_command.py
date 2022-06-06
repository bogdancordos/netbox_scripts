#add netmiko to the local_requirements.txt
from django.utils.text import slugify
from netmiko import ConnectHandler
from django.forms import PasswordInput
from dcim.models import Device, Interface
from ipam.models import IPAddress
from extras.scripts import *


class RunCommand(Script):
    class Meta:
        name = "Run command on Cisco Devices via SSH"
        description = "Run command on Cisco Devices via SSH"
        field_order = ['device', 'input_username', 'input_pass', 'input_command']


    device = ObjectVar(
        model=Device,
        query_params={
            'status' : 'active'
        }
    )
    input_username = StringVar(
        description="Enter username:"
    )
    input_pass = StringVar(
        widget=PasswordInput
    )
    input_command = StringVar(
        description="Enter the SSH command:"
    )


    def run(self, data, commit):

        address = data["device"].primary_ip
        device_ip = str(address.address.ip)

        cisco1 = {
            "device_type": "cisco_ios",
            "host": device_ip,
            "username": data['input_username'],
            "password": data['input_pass'],
        }

        command = data['input_command']

        with ConnectHandler(**cisco1) as net_connect:
            output = net_connect.send_command(command)



            self.log_success("View the information bellow")
        return '' .join(output)
