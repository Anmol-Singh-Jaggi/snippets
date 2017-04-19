First of all, disable every effect except the following:

 - Fade in
 - Fade out
 - Adjustable Fade
 - Studio Fade Out


Now, the steps to edit songs in Audacity:

 - Import audio.
 - Save as project (because Audacity hangs **too much**).
 - Note down the segments of the song which you **dont** like in a text file, by playing the file in VLC. Make these observations as accurate as possible.
 - For all the unwanted segments between timestamps `t1` - `t2`, do the following:
   - Delete the segment by applying *Split Delete* to it.
   - Apply *Fade Out* to `t1-00:00:15` and *Fade In* to `t2+00:00:15`.
 - Add a new track; *Tracks* -> *Add New* -> *Stereo Track*.
 - Now, starting from the end of the track in reverse direction, do the following for every clipping:
   - Move the segment `t2+00:00:15` to the new track using *Split*.
   - Shift the above segment to the left until it is in sync with the ending of `t1-00:00:15`.
   - Shift the rest of the track present on the right of `t2+00:00:15` to the left until it is touching the clipping. The easiest way of doing this is to select the empty portion (Use 'Ctrl-click' to select both the tracks!) and apply *Cut*.
 - Finally in the end of the song, if it ends abruptly, apply the *Studio Fade Out* to the last 30 seconds or so.
 - Export as an mp3 (quality = 'Extreme') or as an .ogg (quality = 5).
 - **Keep saving the project in between as Audacity hangs too much.**
