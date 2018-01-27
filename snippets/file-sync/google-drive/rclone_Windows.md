```
set DIRNAME=Docs
set DIRPATH=anmol/%DIRNAME%
set LOCALPATH=D:/%DIRPATH%
set REMOTEPATH=gdrive:/%DIRPATH%
```

## Upload files from local to remote; doesn't delete remote files not present on local
```
rclone copy %LOCALPATH% %REMOTEPATH% --ignore-size -cn
```

## Upload files from local to remote; deletes remote files not present on local (making remote exactly same as local)
```
rclone sync %LOCALPATH% %REMOTEPATH% --ignore-size -cn
```

## Tells the difference between local and remote
```
rclone check %LOCALPATH% %REMOTEPATH%
```

## Download files from remote to local.
```
rclone copy %REMOTEPATH% %LOCALPATH% --ignore-size -cn
```
