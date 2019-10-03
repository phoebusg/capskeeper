# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 10:26:00 2017

@author: panos
mod for OS X PhoebusG
"""

#Libraries we need
import pyxhook
import time
import subprocess
import pyautogui
import os

#initialization
capsstatus = 0
capsstatusnew = 0
print("This is the current path:")
print(os.getcwd())
capsstatus = subprocess.run(["checkModifierKeys", "capslock"],shell=True)    #THIS IS WHERE WE GET THE INITIAL CAPS LOCK STATUS

#This function is called every time a key is presssed
def kbeventdown( event ):
    global capsstatus
   #WHEN LEFT cmd IS PRESSED, WE CHECK THE CAPS LOCK STATUS
    if event.Key == "cmd_l":
        print ("Shift Key Pressed!")
        capsstatus = subprocess.run(["checkModifierKeys", "capslock"],shell=True)    #THIS IS WHERE WE GET THE CAPS LOCK STATUS    
        if capsstatus == "2":
         print ("CAPS LOCK STATUS: OFF")
        if capsstatus == "3":
         print ("CAPS LOCK STATUS: ON")

#This function is called every time a key is released        
def kbeventup( event ):
        
    #print key info 
    #WHEN cmd LEFT IS RELEASED, WE CHECKED IF THE CAPS LOCK STATUS HAS CHANGED, TO TAKE THE APPROPRIATE ACTION
    if event.Key == "cmd_l":
        print ("Shift Key Released!")
        time.sleep(0.1) # I PUT A SLIGHT DELAY BECAUSE MANY TIMES IT COULDNT CATCH THE CHANGE OF THE STATUS
        capsstatusnew = subprocess.run(["checkModifierKeys", "capslock"],shell=True)     #HERE IS WHERE WE GET THE NEW STATUS   
        if capsstatusnew == capsstatus:  #HERE IS WHERE WE COMPARE THE STATUS BEFORE AND AFTER THE LANGUAGE CHANGE
         print ("CAPS LOCK STATUS DIDN'T CHANGE, I WONT DO ANYTHING!")
         
         
        else:
         print ("CAPS LOCK STATUS HAS CHANGED, SENDING CAPSLOCK KEY PRESS...")    
         pyautogui.press('capslock')


#Create hookmanager
hookman = pyxhook.HookManager()
#Define our callback to fire when a key is pressed down
hookman.KeyDown = kbeventdown

#Define our callback to fire when a key is released
hookman.KeyUp = kbeventup

#Hook the keyboard
hookman.HookKeyboard()
#Start our listener
hookman.start()
    
#Create a loop to keep the application running
running = True
while running:
    time.sleep(0.1)

#Close the listener when we are done
hookman.cancel()
