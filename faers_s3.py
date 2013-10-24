from flask import Flask
from flask import render_template
app = Flask(__name__)

from scraper.scraper import get_latest_links
from uploader.uploader import s3upload, list_keys

def sync_faers():
    links = get_latest_links()
    for filename, url in links.items():
        try:
            s3upload(filename, url)
        except:
            print "Error uploading %s" % filename
            
@app.route("/")
def list():
    files = list_keys()
    return render_template('list.html', files=files)

if __name__ == "__main__":
    app.debug = True
    
    app.run()