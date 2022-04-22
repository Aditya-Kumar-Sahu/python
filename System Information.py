# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 09:00:01 2021

@author: hp
"""
# Windows Management Instrumentation
# to get system information
import wmi
c=wmi.WMI()
my_system=c.Win_ComputerSystem()[0]

print(f"Manufacture: {my_system.Manufacture}")
print(f"Model: {my_system.Model}")
print(f"Name: {my_system.Name}")
print(f"Number of Processors: {my_system.NumberOfProcessors}")
print(f"System Type: {my_system.SystemType}")
print(f"System Family: {my_system.SystemFamily}")
