# Making a simple keylogger and understanding its network trafic

## Step one - making the virus

I was very interested in understanding viruses and I dicided on making a simple keylogger that would use Discords servers to send information to. 

I used pynput to capture the keys and pyautogui to take a inital screenshot of the users screen and send it to confirm a connection between the script and the discord webhook. 

Then I made the keylogger slightly more complicated so where if it detected an @gmail.com it would send an alert of an email and any characters and words it detected near the email it would mark as a potential password and send it. 

This allowed me to have a little fin while practicing my python skills for the next part of the project. 

## Step two - understanding the viruses network packets 
