import requests
from urllib.parse import quote
import pprint
pp=pprint.PrettyPrinter(indent=4)

devicetoken = '240A90CC-4C40-32C7-B44E-D4CF9E670605'


def blb_search_key(keyword):
    link = f'https://api.sfacg.com/search/novels/result' \
           f'?q={quote(keyword)}' \
           '&expand=novels,comics,albums,chatnovelstags,typeName,authorName,intro,latestchaptitle,latestchapintro,tags,sysTags' \
           '&sort=hot' \
           '&page=0' \
           '&size=12' \
           '&systagids='
    sfsecurity = f'nonce=FA8B7BE2-0277-45D1-92D0-54D69F604AEE&timestamp=1651548657250&devicetoken={devicetoken}&sign=B2DFF06ED5F8B5661E7EE1A74691A9BA'

    headers = {
        'accept-charset': 'UTF-8',
        'authorization': 'Basic YW5kcm9pZHVzZXI6MWEjJDUxLXl0Njk7KkFjdkBxeHE=',
        'accept': 'application/vnd.sfacg.api+json;version=1',
        'user-agent': 'boluobao/4.8.42(android;25)/XIAOMI/240a90cc-4c40-32c7-b44e-d4cf9e670605/XIAOMI',
        'sfsecurity': sfsecurity,
        'accept-encoding':	'gzip'
    }

    resp = requests.get(url=link, headers=headers)
    pp.pprint(resp.json())


def blb_search_category(novelId):
    link = f'https://api.sfacg.com/novels/{novelId}/dirs?expand=originNeedFireMoney'
    sfsecurity = f'nonce=AAF20A8B-E275-4253-9466-D2E3DFFF2175&timestamp=1651549644606&devicetoken={devicetoken}&sign=B33E1D45B2DB4EBC30B5FDE87868D489'

    headers = {
        'accept-charset': 'UTF-8',
        'authorization': 'Basic YW5kcm9pZHVzZXI6MWEjJDUxLXl0Njk7KkFjdkBxeHE=',
        'accept': 'application/vnd.sfacg.api+json;version=1',
        'user-agent': 'boluobao/4.8.42(android;25)/XIAOMI/240a90cc-4c40-32c7-b44e-d4cf9e670605/XIAOMI',
        'sfsecurity': sfsecurity,
        'accept-encoding':	'gzip'
    }

    resp = requests.get(url=link, headers=headers)
    pp.pprint(resp.json())


if __name__ == '__main__':
    blb_search_key('斗破苍穹')

    # blb_search_category('142361')
