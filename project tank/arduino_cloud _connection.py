#%%
import torch
import matplotlib
from arduino_iot_cloud import ArduinoCloudClient
import time
import logging

import sys
sys.path.append("lib")

from arduino_iot_cloud import ArduinoCloudClient

DEVICE_ID = b"3312ee93-efe5-462d-b470-6d75aed7d681"
SECRET_KEY = b"ELUyuZiPvg14a9QpE6osVllyb"

def logging_func():
    logging.basicConfig(
        datefmt="%H:%M:%S",
        format="%(asctime)s.%(msecs)03d %(message)s",
        level=logging.INFO,
    )   

# This function is executed each time the "test_switch" variable changes 
def on_switch_changed(client, value):
    print("Switch Pressed! Status is: ", value)

if __name__ == "__main__":

    logging_func()
    client = ArduinoCloudClient(device_id=DEVICE_ID, username=DEVICE_ID, password=SECRET_KEY)

    client.register("test_value")  
    client["test_value"] = 25
    client.register("test_switch", value=False, on_write=on_switch_changed)
    
    client.start()