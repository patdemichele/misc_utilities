This is a repo where I'll put any day-to-day utilities I write.

# Shuffle

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

# Py2048

This is a Python implementation of the popular game 2048. It can be run in the command line with `python Py2048.py`. Warning: this was written in Python 2.7, so it uses the `raw_input` method for user input. If you'd like to run it with Python 3.x, modify `Py2048.py` to use `input` instead of `raw_input`.

TODO
* Refine `Py2048.render()` to better than just spitting out the NumPy array.
* Add a GUI (maybe)
* Make a bot that is good at playing 2048 (this was the original purpose of making this)