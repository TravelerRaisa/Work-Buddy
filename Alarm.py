import datetime # Importing datetime module to get the current time
from playsound import playsound # Importing playsound to play the alarm sound
import time # Importing time module to add delays and manage timing in the program

# Display the title of the alarm clock
print(" \n\t\t\t\t Alarm Clock🔊\n ")

# Taking user input for alarm time
alarmhour = int(input(" Enter Alarm Hour (1-12):  "))
alarmmin = int(input(" Enter Alarm Minutes:  "))
alarmtime = input(" Enter am/pm:  ").lower()

# Handle "am" and "pm" correctly
if alarmtime == "pm" and alarmhour != 12:  
    alarmhour += 12 # Convert PM hours to 24-hour format (except 12 PM, which remains 12)
elif alarmtime == "am" and alarmhour == 12:
    alarmhour = 0 # Midnight (12 AM) should be converted to 00:00 in 24-hour format
    
# Infinite loop to keep checking the current time
while True :
    # Check if the current hour and minute match the alarm time
    if alarmhour == datetime.datetime.now().hour and alarmmin == datetime.datetime.now().minute :
       print(" 🎇Alarm Ringing! ")
       playsound("Alarm Clock\zapsplat_multimedia_game_sound_harsh_alarm_bell_ring_78336.mp3")
       break # Exiting the loop (this prevents continuous checking)
       
    else: 
       print(" You will find alarm in right time😴 ")
       time.sleep(3)
       