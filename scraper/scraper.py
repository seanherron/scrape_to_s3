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

def get_archive_links():
    page = requests.get('http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/ucm083765.htm')
    tree = html.fromstring(page.text)
    aers_2012_legacy = tree.xpath("//h2[contains(text(), 'Legacy AERS Data Files 2012')]/following-sibling::ul/li")
    archive_files = tree.xpath("//h4[contains(text(), '2004-2011 Quarterly Data Files')]/following-sibling::blockquote/ul/li")
    links = dict()
    for link in aers_2012_legacy:
        rawstr = html.tostring(link)
        tree = html.fromstring(rawstr)
        title = tree.xpath('//a/linktitle/text()')
        if title == []:
            title = str(tree.xpath('//a/text()')[0].encode('utf-8')).split('(')[0]
        else:
            title = title[0]
        url = tree.xpath('//a/@href')[0]
        url = 'http://www.fda.gov' + url
        links[title] = url
    for link in archive_files:
        rawstr = html.tostring(link)
        tree = html.fromstring(rawstr)
        title = tree.xpath('//a/linktitle/text()')
        if title == []:
            title = str(tree.xpath('//a/text()')[0].encode('utf-8')).split('(')[0]
        else:
            title = title[0]
        url = tree.xpath('//a/@href')[0]
        url = 'http://www.fda.gov' + url
        links[title] = url
    return links
    
def link_creator():
    latest_links = get_latest_links()
    archive_links = get_archive_links()
    merged_links = dict(latest_links.items() + archive_links.items())
    return merged_links