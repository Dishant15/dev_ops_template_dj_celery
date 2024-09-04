#!/bin/bash

LOG () {
    echo $'\n'
    echo "################################################################"
    echo "$1"
    echo "################################################################"
    echo $'\n'
}


# sudo apt-get remove docker docker-engine docker.io containerd runc 

LOG "APT Update......"
sudo apt update

sleep 1

LOG "Installing certificates......"
sudo apt install ca-certificates curl gnupg lsb-release -y

sleep 1

LOG "Creating Directory /etc/apt/keyrings......"
sudo mkdir -p /etc/apt/keyrings

sleep 1

LOG "Downloading Docker KEY......"
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

sleep 1

LOG "Downloading https://download.docker.com/linux/ubuntu......"
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sleep 1

LOG "APT Update......"
sudo apt update 

sleep 1

LOG "Installing Docker......"
sudo apt install docker-ce docker-ce-cli containerd.io docker-compose-plugin -y
 
sleep 1
LOG "Docker Installed"


