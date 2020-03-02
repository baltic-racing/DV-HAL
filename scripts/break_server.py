#!/usr/bin/env python
from __future__ import print_function
from hal.srv import FootBreak, FootBreakResponse
from airsimCommunicator import get_airsim_communicator
import rospy

airsimclient = None
car_controls = None

def set_airsim_client_and_controls(client, controls):
    global airsimclient, car_controls
    airsimclient = client 
    car_controls = controls

def set_foot_brake_pressure(req):

    global airsimclient, car_controls

    print("Request is", req)

    car_current_break_value  =  car_controls.brake
    car_controls.brake = req.setBreakPressure
    airsimclient.setCarControls(car_controls)
    
    #TODO Implement exception handling if new throttle value could'nt get set
    #TODO Implement maximum steering range check

    #could we set it?
    car_current_break_value =  car_controls.brake
    return FootBreakResponse(car_current_break_value)