```
set DIRNAME=Software
set DIRPATH=anmol/%DIRNAME%
set LOCALPATH=D:/%DIRPATH%
set DISKPATH=F:/%DIRPATH%
```

## Copy files from local to disk; doesn't delete files on disk not present on local
```
rclone copy %LOCALPATH% %DISKPATH% --ignore-size -cn
```

## Copy files from local to disk; deletes files on disk not present on local (making disk exactly same as local)
```
rclone sync %LOCALPATH% %DISKPATH% --ignore-size -cn
```

## Tells the difference between local and disk
```
rclone check %LOCALPATH% %DISKPATH%
```

## Copies files from disk to local.
```
rclone copy %DISKPATH% %LOCALPATH% --ignore-size -cn
```
