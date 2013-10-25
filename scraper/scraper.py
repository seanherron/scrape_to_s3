def link_creator(scraper_to_run):
    if scraper_to_run == 'fda_faers':
        from fda_faers import scraper
        links = scraper()
        return links
    else:
        links = None
        return links