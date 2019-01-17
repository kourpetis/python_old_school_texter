I am trying to create a Raspberry pi, rawbust, portable, messaging device that uses Minimodem to send and receive texts over VOX radio and have light sensors as inputs ( when a finger covers the light, it detects a press )
I created GUI that does that but not functioning properly. The chars are rolling at the momment but just for the first roll.
I have created a def that reads through a 4067 multiplexer and an mcp3002 the analogue signals to presses but i can't link them to the button functions.

the sensors reading screens are for Temperature, Humidity, Altimeter, Compass.

the best way to operate would be :

while a button is pressed, the chars roll every 0.5 secs in the text area
if the button is released, the last char sets there, appented in a message[], the cursor moves one space right and wait forthe next press, to do the same thing again
if the transmite Button is pressed, pipe message[] to minimodem --tx (this function works well at the moment )

there has to be a backspace function as well ( it works ok up untill now )

any ideas are more than welcome, while i've reached my limits here. 