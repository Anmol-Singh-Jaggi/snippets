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
 - Finally in the end of the song, if it ends abruptly, apply the *Studio Fade Out* to the last 30 seconds or so.
 - Add a new track; *Tracks* -> *Add New* -> *Stereo Track*.
 - Now, starting from the beginning, shift every segment to the left to align with its previous segment in alternating tracks. (1st segment in 1st track, 2nd segment in 2nd track, 3rd segment in 1st track and so on...)
 - Export as an mp3 (quality = 'Extreme') or as an .ogg (quality = 5).
 - **Keep saving the project in between as Audacity hangs too much.**
