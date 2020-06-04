# OpenStack REST

This is a project developed for the Cloud Computing course of Master Degree in Computer Engineering.

## Requirements

The application must allow to schedule the automatic creation of an additional set of VMs of a certain type at peak hours.
The following functionalities must be implemented:

- At initialization, the application should create two new flavors on the platform, one _standard_ flavor and a _large_ flavor with more resources;
- At scheduled times, the application should trigger the creation of new VMs, based on an existing image;
- At the end of the scheduled peak period, the application should destroy the additional VMs.

In order to allow system administrator to schedule for the creation of new VMs, the application must expose a REST interface to schedule the peak period and select the flavor and the image for the VMs to be created.

## Contributors
F. Barbarulo, D. Casu, B.T. Gurmesa, G.B. Rolandi 
