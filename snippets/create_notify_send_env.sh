#!/bin/bash
# Create a new file containing the values of the environment variables
# required for notify-send to work.
# This script is supposed to be scheduled to run at startup.

notify_send_env_path="$HOME/.notify_send_env"

rm -f "${notify_send_env_path}"
touch "${notify_send_env_path}"
chmod 600 "${notify_send_env_path}"

# Array of the environment variables.
env_vars=("DBUS_SESSION_BUS_ADDRESS" "XAUTHORITY" "DISPLAY")

for env_var in "${env_vars[@]}"
do
    echo "$env_var"
    env | grep "${env_var}" >> "${notify_send_env_path}";
    echo "export ${env_var}" >> "${notify_send_env_path}";
done
