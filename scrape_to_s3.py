from scraper.scraper import link_creator
from uploader.uploader import s3upload, list_keys


def sync(scraper_to_run, upload_bucket):
    print "Started Generating Links"
    links = link_creator(scraper_to_run)
    if links is None:
        print "Error with links generation"
        end
    print "Links Generated!"
    print "Starting Uploads"
    for filename, url in links.items():
        try:
            s3upload(upload_bucket, filename, url)
        except:
            print "Error uploading %s" % filename
    print "Uploads done!"
    

# Start by prompting for what the user wants to do
print 'Type the name of the scraper you wish to run'
scraper_to_run = raw_input()
print 'We will run the %s scraper' % scraper_to_run

print 'What bucket should we upload to?'
upload_bucket = raw_input()
print 'We will upload to %s' % upload_bucket

print 'What filename should we output S3 URLs to? Leave blank for default (s3files.txt)'
output_file = raw_input()
if output_file == '':
    output_file = 's3files.txt'
print 'Writing output to %s' % output_file

print 'Ok, starting now!'
sync(scraper_to_run, upload_bucket)
print 'Done with uploading! Now generating a list of URLs'
list_keys(upload_bucket, output_file)
print 'You are all done!'