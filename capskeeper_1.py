# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 10:26:00 2017

@author: panos
"""

#Libraries we need
import pyxhook
import time
import commands
import pyautogui

#initialization
capsstatus = 0
capsstatusnew = 0
capsstatus = commands.getoutput('xset q | grep LED')[65]    #THIS IS WHERE WE GET THE INITIAL CAPS LOCK STATUS    
#This function is called every time a key is presssed
def kbeventdown( event ):
    global capsstatus
   #WHEN LEFT ALT IS PRESSED, WE CHECK THE CAPS LOCK STATUS
    if event.Key == "Alt_L":
        print "ALT TIS EI!"
        capsstatus = commands.getoutput('xset q | grep LED')[65]    #THIS IS WHERE WE GET THE CAPS LOCK STATUS    
        if capsstatus == "2":
         print "CAPS LOCK OFF"
        if capsstatus == "3":
         print "CAPS LOCK ON"

#This function is called every time a key is released        
def kbeventup( event ):
        
    #print key info
    #WHEN SHIFT LEFT IS RELEASED, WE CHECKED IF THE CAPS LOCK STATUS HAS CHANGED, TO TAKE THE APPROPRIATE ACTION
    if event.Key == "Shift_L":
        print "ΤΟ SHIFT ΑΦΕΘΗΚΕ!"
        capsstatusnew = commands.getoutput('xset q | grep LED')[65]     #HERE IS WHERE WE GET THE NEW STATUS   
        if capsstatusnew == capsstatus:  #HERE IS WHERE WE COMPARE THE STATUS BEFORE AND AFTER THE LANGUAGE CHANGE
         print "ΔΕΝ ΚΑΝΩ ΤΙΠΟΤΑ"
         
         
        else:
         print "CAPSLOCK CHANGED"    
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