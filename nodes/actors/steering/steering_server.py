#!/usr/bin/env python
from __future__ import print_function
from hal.srv import SteeringSrv, SteeringSrvResponse
from airsimCommunicator import get_airsim_communicator
import rospy

airsimclient = None
car_controls = None

def set_airsim_client_and_controls(client, controls):
    global airsimclient, car_controls
    airsimclient = client 
    car_controls = controls

def set_steering_angle(req):

    global airsimclient, car_controls

    print("Request is", req)

    car_current_steering_angle  =  car_controls.steering
    car_controls.steering = req.setSteeringAngle
    airsimclient.setCarControls(car_controls)
    
    #TODO Implement exception handling if new throttle value could'nt get set
    #TODO Implement maximum steering range check

    #could we set it?
    car_current_steering_angle =  car_controls.steering
    return SteeringSrvResponse(car_current_steering_angle, 1)