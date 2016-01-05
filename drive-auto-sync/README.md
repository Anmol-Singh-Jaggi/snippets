# drive-auto-sync

Automatically upload data to your Google Drive account at specified time intervals.


**Dependencies:**
 - `pip install --upgrade google-api-python-client`

**Usage:**
 - Download your *`client_secrets.json`* file from the Google Developer Console and keep it in this directory.
 - Modify the *`file_list.json`* file as per your needs. For new files, keep the `fileId` empty and `parentId` as the ID of the Drive directory in which the file has to be inserted.
 - Modify *`custom_cmds_pre.sh`* and *`custom_cmds_post.sh`* as per your needs.
 - For scheduling it, execute:
   - `crontab -e`
   - `0 17 * * * cd /media/Data/anmol/coding/github/snippets/drive-auto-sync && ./run.sh` (Run every day at 5:00 pm.)
