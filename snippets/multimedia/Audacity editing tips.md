First of all, disable every effect except the following:

 - Fade in
 - Fade out
 - Adjustable Fade
 - Studio Fade Out


Now, the steps to edit songs in Audacity:

 - Import audio.
 - Save as project (because Audacity hangs *too much*).
 - Note down the segments of the song which you **dont** like in a text file.
 - Let the first segment be from *t1* to *t2*.
 - Apply *Fade out* to `t1-00:00:15` and *Fade in* to `t2+00:00:15`.
 - Repeat the above operation for all the segments.
 - Delete all the segments (identify them by the surrounding fade-in/fade-out effects).
 - Apply *Split new* to create a new track.
 - Shift the portion after `t1+00:00:15` to the left until it is in sync with the ending of `t1+00:00:15`.
 - Finally in the end of the song, if it ends abruptly, apply the *Studio Fade out* to the last 30 seconds or so.
 - Export as an mp3 or as an .ogg (quality = 5).
 - **Keep saving the project in between as Audacity hangs too much.**
