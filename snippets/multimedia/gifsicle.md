## Extract frames from gif
    gifsicle -U -e out.gif

## Combine frames to gif
    gifsicle ./* -O3 -o out.gif

## Compress gif
    gifsicle -U in.gif -O3 -o out.gif
