#!/bin/bash

# print env variables to this file to make sure the env variables can be used with docker
# https://stackoverflow.com/questions/27771781/how-can-i-access-docker-set-environment-variables-from-a-cron-job
# https://ypereirareis.github.io/blog/2016/02/29/docker-crontab-environment-variables/
printenv  >> /etc/environment

cron && tail -f /var/log/cron.log