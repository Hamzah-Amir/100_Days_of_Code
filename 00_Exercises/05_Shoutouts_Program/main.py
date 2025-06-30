# Write a program that will give shoutouts to all the people in a list.
import win32com.client
# Ensure you have the pywin32 package installed to use win32com.client

def shoutout():

    names  = ["Hamza","Sana","Ali","Ayesha","Hassan","Fatima"]
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    for name in names:
        speaker.Speak(f"Shoutout to {name}!")

shoutout()  
# This program uses the SAPI.SpVoice to give shoutouts to each name in the list.
# Make sure you have the necessary permissions to use the speech synthesis feature.