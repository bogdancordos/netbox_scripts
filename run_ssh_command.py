#add netmiko to the local_requirements.txt
from django.utils.text import slugify
from netmiko import ConnectHandler
from django.forms import PasswordInput
from extras.scripts import *


class RunCommand(Script):
    class Meta:
        name = "Run command on Cisco Devices via SSH"
        description = "Run command on Cisco Devices via SSH"
        field_order = ['input_ip', 'input_username', 'input_pass', 'input_command']


    input_ip = IPAddressVar(
        description="Enter the IP Address:"

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

        cisco1 = { 
            "device_type": "cisco_ios",
            "host": data['input_ip'],
            "username": data['input_username'],
            "password": data['input_pass'],
        }

        command = data['input_command']

        with ConnectHandler(**cisco1) as net_connect:
            output = net_connect.send_command(command)

            self.log_success(output)
        return "Success"
