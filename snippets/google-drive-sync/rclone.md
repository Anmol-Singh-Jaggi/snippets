    DIRPATH="/anmol/DTU/Sems/4/ADA"

## Upload files from local to remote; doesn't delete remote files not present on local
    rclone copy "/home/anmol/Data${DIRPATH}" "remote:${DIRPATH}" --ignore-size -cn

## Upload files from local to remote; deletes remote files not present on local (making remote exactly same as local)
    rclone sync "/home/anmol/Data${DIRPATH}" "remote:${DIRPATH}" --ignore-size -cn

## Tells the difference between local and remote
    rclone check "/home/anmol/Data${DIRPATH}" "remote:${DIRPATH}"

## Download files from remote to local.
    rclone copy "remote:${DIRPATH}" "/home/anmol/Data${DIRPATH}" --ignore-size -cn
