# piRadio
Raspberry Pi internet radio for 3.2TFT screen

 - Using MPD / MPC to playback mp3 and internet radio stations
 - Utilizing buttons on display

## The hardware

 - RaspberryPI 2 or 3
 - TFT Touchscreen display 
   http://www.waveshare.com/wiki/3.2inch_RPi_LCD_(B)#Image
   

## The software
 
### Linux and drivers for TFT display
 
Simplest way is to burn this image: http://www.waveshare.com/wiki/3.2inch_RPi_LCD_(B)#Image

#### Check before starting
- make sure /dev/input/touchscreen device is present
- enabled and working network connection 
- you have calibrated your touchscreen
- you can connect to your Pi via SSH (pi@<local.ip.address>)

### Python 

Update and install mpd / mpc


`
sudo apt-get install mpd mpc python-mpc
`


   