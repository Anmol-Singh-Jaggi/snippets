# Instructions to create archive using `tar`

 - Input folder name = "Software"
 - First cd into the parent directory of the input
 - Then execute the following steps:  

## Commands to create archive
    mkdir archive
    input="Software"
    target="archive/$input.tar"
    tar --create --file="$target" "$input"

## With progress bar
    input_size=`du -sk "$input" | cut -f 1`
    tar --create --file=- "$input" | pv -s ${input_size}k > "$target"

------------------

## Commands to extract archive
    mkdir extracted
    cat "$target" | tar --extract --directory=extracted --file=-

## With progress bar

    input_size=`du -b "$target" | cut -f 1`
    cat "$target" | pv -s ${input_size} | tar --extract --directory=extracted --file=-


------------------
------------------
------------------

# Instructions to create multi-archive using `tar` and `split`

## Commands to create archive
    # Size of a single file in the resultant archive
    per_file_size=3G
    tar --create --file=- "$input" | split --numeric-suffixes --bytes=$per_file_size - "$target"

## With progress bar
    tar --create --file=- "$input" | pv -s ${input_size} | split --numeric-suffixes --bytes=$per_file_size - "$target"

------------------

## Command to extract archive
    cat "$target"* | tar --extract --directory=extracted --file=-

## With progress bar
    input_size=`du -b archive | cut -f 1`
    cat "$target"* | pv -s ${input_size} | tar --extract --directory=extracted --file=-


------------------
------------------
------------------

# Instructions to copy multiple tar files to the pen drive

 - cd to the archive directory and execute the following as a script:

```
# Script starts

dest=/media/anmol/Anmol-Sandisk
copy_file()
{
    file="`pwd`/$1"
    file_size=`du -b "$file" | cut -f 1`
    `cat "$file" | pv -s ${file_size} > "$dest/$1"`
}

for file in * ; do
    echo "Copying $file ..."
    copy_file "$file"
done

# Script ends
```
