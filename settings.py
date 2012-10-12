# Settings file for the incremental dumps

# The temporary directory to store the incremental dumps
# Note: Incremental dumps gets deleted after its uploaded.
tempdir = "" # No slash at the end

# Archive.org's S3-like API keys
# (Get yours at http://archive.org/account/s3.php)
accesskey = ""
secretkey = ""

# URL-to-the-incr-dumps
hosturl = "http://dumps.wikimedia.your.org/other/incr" # No slash at the end
rsynchost = "ftpmirror.your.org::wikimedia-dumps/other/incr" # No slash at the end
wgethost = "http://dumps.wikimedia.your.org/other/incr" # No slash at the end

# Archive.org matters
collection = ""
mediatype = ""
# You don't really need to change this
sizehint = "107374182400" # 100GB
