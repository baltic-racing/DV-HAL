#!/usr/bin/env python
from __future__ import print_function
from hal.srv import Throttle, ThrottleResponse
from airsimCommunicator import get_airsim_communicator
import rospy
import airsim

airsimclient = None
car_controls = None

def set_airsim_client_and_controls(client, controls):
    global airsimclient, car_controls
    airsimclient = client 
    car_controls = controls

def set_throttle(req):
    global airsimclient, car_controls

    # get state of the car
    print("Request is", req)

    car_current_steering = car_controls.steering
    car_current_throttle  = car_controls.throttle

    print("Steering: ",car_current_steering," Throttle: ",car_current_throttle)

    car_controls.throttle = req.setThrottle
    airsimclient.setCarControls(car_controls)
    #TODO Implement exception handling if new throttle value could'nt get set

    #could we set it?
    car_current_throttle = car_controls.throttle
    return ThrottleResponse(car_current_throttle, 1)