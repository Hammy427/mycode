#!/usr/bin/env python3
""""Moving files and Folders Lab """
# Import required shutil module
import shutil
#Import required OS module
import os


# Main Funtion for Lab
def main():

 # Enforce start location
 os.chdir('/home/student/mycode/')

 # Moves raynor.obj to ceph storage
 shutil.move('raynor.obj', 'ceph_storage/')
 # Rename kerrigan.obj file process
 xname = input('What is the new name for kerrigan.obj? ')

main()
