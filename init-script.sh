#!/bin/bash

# Setup system
echo "root:hammer" | chpasswd
cp system-config/sshd_config /etc/ssh/
cp system-config/.pythonrc ~/.pythonrc
cp system-config/.bashrc ~/.bashrc
echo "Restarting sshd service"
/etc/init.d/ssh restart

# Launch application
pushd detector
./detector_automation.sh 
