Bed Scale
=========

This implements a bed scale as explained on http://peter.turczak.de/content/projects/scale/ .
Basically it gives you means of keeping track of several peoples weight sharing the same bed (i.e. families).

Arduino Code
------------
The Arduino software depends on the modified HX711 library from the &quot;parallel&quot; brach of https://github.com/ptwz/HX711 .

Python Code
-----------
The python code needs some initialization in order to work properly.

<code>$ python</code>

<code> >>> import shelve</code>

<code> >>> people=shelve.open("people.shelve")</code>

<code> >>> people['him']=...</code>

<code> >>> people['her']=...</code>

<code> >>> people.close()</code>

Where you would fill the ellipsis by you and e.g. your wifes weight. This way the algorithm has start values to work from.

For running `host_process.py`, redirect its output to a log file.

<code>$ python host_process.py > waage.log</code>

For analyzing the weight changes over time of the previously initializes household members, run `extract_data.py` like so:

<code>$ python extract_data.py > result.dta<code>

The result.dta can then be processed using a spreadsheet or gnuplot.
