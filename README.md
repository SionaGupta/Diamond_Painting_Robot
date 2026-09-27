This is the code for my 2025 Diamond Painting Robot. This robot is a core-xy gantry that places colored resin "diamonds" on a sticky, color-coded chart to form a picture.  

The code is split into two repos: Python and C++. This program communicates with the Arduino using serial communication, allowing me to run color detection software and give commands to the gantry. This program detects which colors go where and sends G-code commands to the Arduino. The Arduino parses these commands into stepper motor movements, along with controlling the pen pick and place. 
