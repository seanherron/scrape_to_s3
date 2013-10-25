from scraper.scraper import link_creator
from uploader.uploader import s3upload, list_keys

def sync():
    print "Started Generating Links"
    links = link_creator()
    print "Links Generated!"
    print "Starting Uploads"
    for filename, url in links.items():
        try:
            s3upload(filename, url)
        except:
            print "Error uploading %s" % filename
    print "Uploads done!"
    
def generate_link_list():
    out = open("s3urls.txt", "w")
    files = list_keys()
    for filename, url in files.items():
        out.write('%s\n' % url)
    out.close()