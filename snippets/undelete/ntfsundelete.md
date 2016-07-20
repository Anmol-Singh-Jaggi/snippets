## Search for all the files matching a regex
    sudo ntfsundelete /dev/sda4 -s -m '*.ogg'

## Recover a file
    # The default recovery location is the home folder.
    # There will be a need to own it - `chown anmol 1.ogg`
    sudo ntfsundelete /dev/sda4 -u -m '1.ogg'
