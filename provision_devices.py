from django.utils.text import slugify

from dcim.choices import DeviceStatusChoices, SiteStatusChoices
from dcim.models import Device, DeviceRole, DeviceType, Manufacturer, Site
from extras.scripts import *


class NewDevice(Script):

    class Meta:
        name = "New Devices"
        description = "Provision new devices"
        field_order = ['site_name', 'switch_count', 'switch_model']

    site_name = ObjectVar(
        description="Name of the site",
        model=Site,
        required=True
    )
    switch_count = IntegerVar(
        description="Number of devices to create"
    )
    manufacturer = ObjectVar(
        model=Manufacturer,
        required=False
    )
    switch_model = ObjectVar(
        description="Device Model",
        model=DeviceType,
        display_field='model',
        query_params={
            'manufacturer_id': '$manufacturer'
        }
    )
    def run(self, data, commit):

        # Create access switches
        switch_role = DeviceRole.objects.get(name='Device Role')
        for i in range(1, data['switch_count'] + 1):
            switch = Device(
                device_type=data['switch_model'],
                site=data['site_name'],
                status=DeviceStatusChoices.STATUS_PLANNED,
                device_role=switch_role
            )
            switch.save()
            self.log_success(f"Created the new device: {switch}")

        return "Success"
