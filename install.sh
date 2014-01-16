#!/bin/bash

# Install the freeze util
echo 'Install frigid'

sudo mkdir /etc/frigid
sudo cp config.yml /etc/frigid/
sudo cp *.sh /etc/frigid/

sudo cp frigid /bin/frigid

