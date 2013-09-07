## README

This is the incremental dumps archiving project. Scripts in this repository are for the archiving of the daily incremental dumps that the Wikimedia Foundation generates (see http://dumps.wikimedia.org/other/incr/).

The scripts in this repository depends on a converter class, a special script located [here](https://github.com/Hydriz/ASConverter) which you would have to download and place in the same directory as your repository's checkout before you can properly run the script (Note: The name of the file **must** be *converter.py*). This converter class allows the easy conversion of raw wiki databases into human-readable format, making it easier for people to find the items on the Internet Archive.

More documentation is available in the repository's wiki.
