#!/bin/bash
sudo apt update
sudo apt full-upgrade
sudo apt-get dist-upgrade
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev -y
wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tar.xz
tar xf Python-3.7.2.tar.xz
cd Python-3.7.2
./configure
make -j 4
sudo make altinstall
sudo apt-get install python-pip
sudo apt-get install python3-pip
npm install
pip3 install pychromecast
pip3 install gtts
# Google Home Service
sudo cp googlehome.service /etc/systemd/system/googlehome.service
sudo systemctl start googlehome.service
sudo systemctl enable googlehome.service
