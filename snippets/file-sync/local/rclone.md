```bash
DIRNAME="Docs"
DIRPATH="anmol/${DIRNAME}"
LOCALPATH="/home/anmol/Data/${DIRPATH}"
DISKPATH="/media/anmol/Seagate Backup Plus Drive/${DIRPATH}"
```

## Copy files from local to disk; doesn't delete files on disk not present on local
```bash
rclone copy "${LOCALPATH}" "${DISKPATH}" --ignore-size -cn
```

## Copy files from local to disk; deletes files on disk not present on local (making disk exactly same as local)
```bash
rclone sync "${LOCALPATH}" "${DISKPATH}" --ignore-size -cn
```

## Tells the difference between local and disk
```bash
rclone check "${LOCALPATH}" "${DISKPATH}"
```

## Copies files from disk to local.
```bash
rclone copy "${DISKPATH}" "${LOCALPATH}" --ignore-size -cn
```
