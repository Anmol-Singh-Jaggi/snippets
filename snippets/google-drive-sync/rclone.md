## Upload files from local to remote; doesn't delete remote files not present on local
    rclone copy "/home/anmol/Data/anmol/Docs" "remote:/anmol/Docs" --ignore-size -cn

## Upload files from local to remote; deletes remote files not present on local (making remote exactly same as local)
    rclone sync "/home/anmol/Data/anmol/Docs" "remote:/anmol/Docs" --ignore-size -cn

## Tells the difference between local and remote
    rclone check "/home/anmol/Data/anmol/Docs" "remote:/anmol/Docs"

## Download files from remote to local.
    rclone copy "remote:/anmol/Docs" "/home/anmol/Data/anmol/Docs" --ignore-size -cn
