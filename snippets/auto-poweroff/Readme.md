Power off system at low power automatically.

First ensure that you can hibernate non-interactively from cron without sudo:  
 - Execute `sudo cp 'com.0.enable-hibernation-from-cron.pkla' '/etc/polkit-1/localauthority/50-local.d/'`

Then, schedule it in cron:  
 - `chmod +x auto-poweroff.sh`.
 - `>> crontab -e`
 - Execute each minute - `* * * * * /path/to/auto-poweroff.sh`.
