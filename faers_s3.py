from scraper.scraper import get_latest_links
from uploader.uploader import s3upload, list_keys

def sync_faers():
    links = get_latest_links()
    for filename, url in links.items():
        try:
            s3upload(filename, url)
        except:
            print "Error uploading %s" % filename