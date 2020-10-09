# When given a URL as a string, parses out just the domain name and returns it as a string.
def domain_name(url):
    if "//www" in url: 
        domain = url.split("www.")[-1].split(".")[0]
        return domain
    elif "//" in url:
        domain = url.split("//")[-1].split(".")[0]
        return domain
    else:
        domain = url.split("www.")[-1].split(".")[0]
        return domain