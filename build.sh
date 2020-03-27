#!/bin/bash
# update system and update packages
sudo apt update
sudo apt full-upgrade
sudo apt-get dist-upgrade
# Install Git
sudo apt install git
# Install latest Node
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs
# Install python3
sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev -y
wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tar.xz
tar xf Python-3.7.2.tar.xz
cd Python-3.7.2
./configure
make -j 4
# Install pip3
sudo make altinstall
sudo apt-get install python-pip
sudo apt-get install python3-pip
# Intall packages
pip3 install pychromecast
pip3 install gtts
# Spotify package
pip3 install spotify-token
pip3 install git+https://github.com/plamere/spotipy.git
# Set Google Home Service
sudo cp googlehome.service /etc/systemd/system/googlehome.service
sudo systemctl start googlehome.service
sudo systemctl enable googlehome.service
