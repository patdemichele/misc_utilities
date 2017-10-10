This is a repo where I'll put any day-to-day utilities I write.

I recently made `shuffle.py` to randomize a playlist I was making for a party.

`shuffle.py` takes a (text) filename as command-line argument (i.e., in `sys.argv[1]`). Running `python shuffle.py filename.txt` will work. It expects a file in the format:
```
Some line
Some line
Some line
[1] info ...
[2] info ...
[3] info ...
```

It then rewrites the file to shuffle all of the `info` while keeping the proper order of numbering.

My original text file was a list of songs (with some headers / etc) at the top. I used `shuffle.py` to shuffle this list.
