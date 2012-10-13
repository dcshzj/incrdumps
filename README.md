## README

This is the incremental dumps archiving project. Scripts in this repository are for the archiving of the daily incremental dumps that the Wikimedia Foundation generates (see http://dumps.wikimedia.org/other/incr/).

The scripts in this repository depends on a converter class, a special script located [here](https://gist.github.com/3878699) which you would have to download and place in the same directory as the script itself before you can properly run the script. This converter class allows the easy conversion of raw wiki databases into human-readable format, making it easier for people to find the items on the Internet Archive. Note: The converter class does not convert all the wiki databases, as it does not currently support wikis in [special.dblist](https://noc.wikimedia.org/conf/special.dblist), in which support for it will be added at a later date.

More documentation is available in the repository's wiki.
