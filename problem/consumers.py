# Import JSON module
import json
# Import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Outputs
from channels.db import database_sync_to_async

# Define the consumer class to send the data through WebsocketConsumer
class ws_consumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.accept()
        #while(True):
        #    res=Outputs.objects.first().op
         #   self.send(json.dumps({'output': res}))
        res=await self.get_name()
        self.send(json.dumps({'output': res}))

    @database_sync_to_async
    def get_name(self):
        return Outputs.objects.first().op
        
        
