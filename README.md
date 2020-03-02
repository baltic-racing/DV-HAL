# Driverless Hardware Abstraction Layer

This ROS-Module recieves sensor data and traforms the data into  standarized output and shares them as ROS mesages for all other DV-Modules to use.
The HAL is also able to control all actors of the car, like steering/braking/accerleration... and makes them accessible via ROS services.