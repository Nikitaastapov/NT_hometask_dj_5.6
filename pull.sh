#!/bin/bash
cd /home/nikita/NT_hometask_dj_5.6
git pull origin cicd
sudo systemctl restart gunicorn
