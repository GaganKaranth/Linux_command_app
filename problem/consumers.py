import json
from channels.generic.websocket import WebsocketConsumer
from .models import Outputs
from .views import rep
from django.core import serializers

class ws_consumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        i=1
        while(True):
            res = Outputs.objects.latest('id')
            serialized_obj = serializers.serialize('json',[res])
            self.send(json.dumps({'output':serialized_obj}))
            i+=1
            if(i==rep):
                break
    #def disconnect(self, event):
      #  return super().disconnect()

            
            
            
        
        
