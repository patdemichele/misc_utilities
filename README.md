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

# Py2048Bot

A simple bot that plays 2048. `python Py2048Bot.py trivial` to observe the bots performance when choosing right/down alternately. `python Py2048Bot.py standard` to observe an attempt at making some nontrivial decisions (it doesn't actually work much better than the trivial).

TODO
* Add more comments (though, the code is pretty simple right now)

# Curlx

A modified version of the Unix `curl` command for the `fish` shell that curls a given URL and saves it in the working directory with filename `X`, where `X` is the longest suffix of the given URL that does not contain a `'/'` character. For example, `curlx http://cs229.stanford.edu/syllabus.html` is equivalent to `curl http://cs229.stanford.edu/syllabus.html > syllabus.html`.

# Maxcurl

Curls given URL, then performs `curlx` on all pdf files that are linked in the HTML of that URL.

TODO
* Adapt Maxcurl to work with relative paths