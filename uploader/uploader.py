from boto.s3.connection import S3Connection
from boto.s3.key import Key
import urllib2
import cStringIO

conn = S3Connection()
bucket = conn.get_bucket('faers')

def s3upload(filename, url):
    if bucket.get_key(filename) is None:
        k = Key(bucket)
        k.key = filename
        file_contents = urllib2.urlopen(url)
        fp = cStringIO.StringIO(file_contents.read())
        k.set_contents_from_file(fp)
        print "Success uploading %s" % filename
    else:
        print "%s already uploaded" % filename
        
def list_keys():
    objects = bucket.list()
    return objects
    