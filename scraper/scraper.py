from lxml import html
import requests
from urllib2 import urlopen

def get_latest_links():
    # This function grabs links from the Latest Quarterly Report Files
    page = requests.get('http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/ucm082193.htm')
    tree = html.fromstring(page.text)
    latest = tree.xpath("//h2[contains(text(), 'FAERS Data Files')]/following-sibling::ul/li")
    links = dict()
    for link in latest:
        rawstr = html.tostring(link)
        tree = html.fromstring(rawstr)
        title = tree.xpath('//a/linktitle/text()')[0]
        url = tree.xpath('//a/@href')[0]
        url = 'http://www.fda.gov' + url
        links[title] = url
    return links