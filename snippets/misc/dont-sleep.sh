#!/usr/bin/env bash

# Command to set the suspend timeout value while on AC
suspend_ac_set_command='gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-timeout'
# Command to set the suspend timeout value while on battery
suspend_battery_set_command=$(echo "$suspend_ac_set_command" | sed "s/-ac-/-battery-/")

# Command to get the suspend timeout value while on AC
suspend_ac_get_command=$(echo "$suspend_ac_set_command" | sed "s/ set / get /")
# Command to set the suspend timeout value while on battery
suspend_battery_get_command=$(echo "$suspend_battery_set_command" | sed "s/ set / get /")

turn_suspend_on()
{
    `$suspend_ac_set_command 1800`
    `$suspend_battery_set_command 1200`
}

turn_suspend_off()
{
    `$suspend_ac_set_command 0`
    `$suspend_battery_set_command 0`
}

get_suspend_state()
{
    echo "AC timeout = `$suspend_ac_get_command`"
    echo "Battery timeout = `$suspend_battery_get_command`"
}



if [ "$1" = "screen" ]
then
    `xset dpms force off`
elif [ "$1" = "off" ]
then
    turn_suspend_on;
    echo "Suspend turned on!"
elif [ "$1" = "on" ]
then
    turn_suspend_off;
    echo "Suspend turned off!"
else
    get_suspend_state;
fi
