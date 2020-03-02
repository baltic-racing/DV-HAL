#!/usr/bin/env python

import airsim

_client = None


def get_airsim_communicator():
    global _client
    if _client is None:
        _client = airsim.CarClient(ip='10.74.3.41')
        _client.confirmConnection()
        _client.enableApiControl(True)
        airsim.CarControls()
    
    return _client

'''
class _AirsimCommunicator(object):
    client = None
    car_controls = None

    def __init__(self):
        if self.client is None:
            self.connect_to_airsim()

    def connect_to_airsim(self):
        print("Run connector")
        # connect to the AirSim simulator 
        #TODO get ip value from the parameter server
        self.client = airsim.CarClient(ip='10.74.3.41')
        print("Car client created")
        self.client.confirmConnection()
        self.client.enableApiControl(True)
        self.car_controls = airsim.CarControls()
'''