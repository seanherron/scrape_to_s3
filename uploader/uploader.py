from boto.s3.connection import S3Connection
from boto.s3.key import Key
import urllib2
import cStringIO

conn = S3Connection()

def s3upload(upload_bucket, filename, url):
    bucket = conn.get_bucket(upload_bucket)
    if bucket.get_key(filename) is None:
        print "Started downloading %s locally" % filename
        k = Key(bucket)
        k.key = filename
        file_contents = urllib2.urlopen(url)
        fp = cStringIO.StringIO(file_contents.read())
        print "Started uploading %s to s3" % filename
        k.set_contents_from_file(fp)
        k.set_canned_acl('public-read')
        print "Success uploading %s" % filename
    else:
        print "%s already uploaded" % filename
        
def list_keys(upload_bucket, output_file):
    bucket = conn.get_bucket(upload_bucket)
    bucket_list = bucket.list()
    out = open(output_file, "w")
    for item in bucket_list:
        item.set_canned_acl('public-read')
        url = item.generate_url(0, query_auth=False, force_http=True)
        out.write('%s\n' % url)
    out.close()
    return True