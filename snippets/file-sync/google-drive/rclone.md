```bash
DIRNAME="Docs"
DIRPATH="/anmol/${DIRNAME}"
LOCALPATH="/home/anmol/Data${DIRPATH}"
REMOTEPATH="remote:${DIRPATH}"
```

## Upload files from local to remote; doesn't delete remote files not present on local
```bash
rclone copy "${LOCALPATH}" "${REMOTEPATH}" --ignore-size -cn
```

## Upload files from local to remote; deletes remote files not present on local (making remote exactly same as local)
```bash
rclone sync "${LOCALPATH}" "${REMOTEPATH}" --ignore-size -cn
```

## Tells the difference between local and remote
```bash
rclone check "${LOCALPATH}" "${REMOTEPATH}"
```

## Download files from remote to local.
```bash
rclone copy "${REMOTEPATH}" "${LOCALPATH}" --ignore-size -cn
```
