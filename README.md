# What is Scrape to S3?

Scrape to S3 is a collection of Python scripts that make it easier to collect a bulk amount of files from a website and upload them to Amazon S3. In particular, it was designed to facilitate the upload of files as part of Amazon's Public Dataset Program.

# Instructions

### Setup Environment
In your virtual environment, you'll need to define two environmental variables, AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY, that have access to the bucket you will be uploading to. Don't forget to also install from requirements.txt!

### Write a scraper
A good start to this would be looking at the example scraper provided in scraper/fda_faers.py. Basically, each scraper should result in a function called ``` scraper() ``` that returns a dictionary with a key/value set of desired filename on S3 (eg. filename.tar.gz) and the source URL to grab it from (eg. http://example.com/filename.tar.gz). You'll also need to edit scraper/scraper.py to have a call for the scraper you have written.

### Run the scraper
From your prompt, run ```python scrape_to_s3.py```. The script will ask you for three items: the name of the scraper to run (eg. ```fda_faers```), the S3 bucket to upload to, and the filename a list of uploaded URLS should be written to. That's it!

# License

The license of the project is the 2-clause BSD license:

```
The MIT License (MIT)

Copyright (c) 2013 Sean Herron

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```