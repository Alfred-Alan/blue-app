from rest_framework.serializers import ModelSerializer
from home_application.models import *
class HostsSerializers(ModelSerializer):
    class Meta:
        model = Hosts
        fields  ='__all__'

class AppsSerializers(ModelSerializer):
    class Meta:
        model = Apps
        fields  ='__all__'