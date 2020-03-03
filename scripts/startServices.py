#!/usr/bin/env python
from __future__ import print_function
from hal.srv import Throttle, ThrottleResponse
from hal.srv import SteeringSrv, SteeringSrvResponse
from hal.srv import FootBrake, FootBrakeResponse

#from airsimCommunicator import get_airsim_communicator

from actors.steering import steering_server
from actors.throttle import throttle_server
from actors.brake import brake_server

import rospy
import airsim

client = None
controls = None

def startServices():
    rospy.init_node('car_control_node')
    s = rospy.Service('set_brake_value', FootBrake, brake_server.set_foot_brake_pressure)
    print ('Brake service online')
    s = rospy.Service('set_steering_angle', SteeringSrv, steering_server.set_steering_angle)
    print ('Steering service online')
    s = rospy.Service('set_throttle', Throttle, throttle_server.set_throttle)
    print ('Throttle service online')

    rospy.spin()

if __name__ == "__main__":
    # connect to the AirSim simulator 
    client = airsim.CarClient(ip='10.74.3.41')
    client.confirmConnection()
    client.enableApiControl(True)
    controls = airsim.CarControls()

    steering_server.set_airsim_client_and_controls(client, controls)
    throttle_server.set_airsim_client_and_controls(client, controls)
    brake_server.set_airsim_client_and_controls(client, controls)
    startServices()