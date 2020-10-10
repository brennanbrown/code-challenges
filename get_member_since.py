from urllib.request import urlopen
import re

def get_member_since(username):
    url = 'https://www.codewars.com/users/{}'.format(username)
    html = str(urlopen(url).read())
    date = re.search('Member Since:</b>(.*?)</div>', html)
    return date.group(1)