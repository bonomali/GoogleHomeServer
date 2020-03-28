#!/bin/bash
#sudo -u homeassistant -H -s
#source /srv/homeassistant/bin/activate
#hass
sudo -u homeassistant -H -s
cd /srv/homeassistant
python3 -m venv .
source bin/activate
hass
