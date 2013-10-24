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
        k.set_canned_acl('public-read')
        print "Success uploading %s" % filename
    else:
        print "%s already uploaded" % filename
        
def list_keys():
    files = {}
    bucket_list = bucket.list()
    for item in bucket_list:
        item.set_canned_acl('public-read')
        url = item.generate_url(0, query_auth=False, force_http=True)
        files[item.name] = url
    return files
       
        
    