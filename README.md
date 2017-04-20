# capskeeper
This is a simple script, so that we can keep the CAPS LOCK status while switching languages with the Alt+Shift L keys, in Ubuntu Unity.

It uses the pyxhook module to listen to the key presses even in the background (included), and it also takes advantage of the pyautogui library to automatically press CAPS LOCK button, if needed (needs to be installed separatelly, with the command pip install -U pyautogui).
