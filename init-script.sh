#!/bin/bash

# Setup environment
echo "root:hammer" | chpasswd
cp system-config/sshd_config /etc/ssh/
cp system-config/.pythonrc ~/.pythonrc
cp system-config/.bashrc ~/.bashrc

pushd detector
. detector_automation.sh 
