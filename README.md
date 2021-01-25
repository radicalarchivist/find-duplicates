# find-duplicates
A utility that QUICKLY and recursively scans a folder for duplicate files
v.0.1
2020 by radicalarchivist

### Setup
    $ pip install -r requirements.txt

### Usage  
    find-duplicates [-o OUTPUT-FILE] SCAN-DIR...
    find-duplicates --help
    find-duplicates --version

    Options:
      SCAN-DIR                              Directory to be scanned, seperate multiple dirs with a space.
      -o --output OUTPUT-FILE               Send output to a csv file
      -h --help                             Show this screen
      --version                             Show version info

### Examples

Scan a single directory for duplicates

    # *nix/Mac
    $ find-duplicates /home/user/Videos

    # Windows
    C:\find-duplicates path> C:\Path\to\Python.exe find-duplicates C:\home\user\Videos

Scan multiple directories for duplicates and send output to a .csv file

    # *nix/Mac
    $ find-duplicates -o duplicates.csv /home/user/Videos /home/user/Pictures/gifs

    # Windows
    C:\find-duplicates path> C:\Path\to\Python.exe find-duplicates o duplicates.csv C:\home\user\Videos C:\home\user\Pictures\gifs

### Support RadicalArchivist
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/N4N53F7TD)