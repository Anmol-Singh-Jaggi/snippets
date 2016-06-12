#!/usr/bin/env bash

# Notifies the user if the battery is low.
# Executes some command (like hibernate) on critical battery.
# This script is supposed to be called from a cron job.
# Currently works only when scheduled using root cron: `sudo crontab -e`
# If you change this script's name/path, don't forget to update it in crontab !!

level=$(cat /sys/class/power_supply/BAT1/capacity)
status=$(cat /sys/class/power_supply/BAT1/status)

# Exit if not discharging
if [ "${status}" != "Discharging" ]; then
  exit 0
fi


# Source the environment variables required for notify-send to work.
. /home/anmol/.env_vars

low_notif_percentage=20
critical_notif_percentage=100
critical_action_percentage=95


if [ "${level}" -le ${critical_action_percentage} ]; then
  systemctl hibernate
  exit 0
fi

if [ "${level}" -le ${critical_notif_percentage} ]; then
  notify-send -i '/usr/share/icons/gnome/256x256/status/battery-caution.png' "Battery critical: ${level}%"
  exit 0
fi

if [ "${level}" -le ${low_notif_percentage} ]; then
  notify-send -i '/usr/share/icons/gnome/256x256/status/battery-low.png' "Battery low: $level%"
  exit 0
fi
