# cookie = '_T_WM=15676460302; SCF=AqiOrjk4aSvbMg4JYcHZsIRRBZUe0PjQZiWoqklRniOlNPqDM61v1VVncAwprT3NRqHknQZ0sxkDrCsZVCES20s.; SUB=_2A25zcEJODeRhGeBH6FAU9ybJwz2IHXVQm24GrDV6PUJbktCOLXP2kW1NQdzc1KIKKdEDDpNip0SsFAQQj7OLuoz_; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF8I8fT-HyNSg6Y5_vfXy0O5JpX5KzhUgL.Foq4e0zfS0nf1h22dJLoIEMLxK-LB--L1h.LxKnL12zLBK-LxKqL1-2L1KqLxK.L1KnLBoSkCXYt; SUHB=0auQI-2Zcq0w60; SSOLoginState=1584673311'
#
# cookies = dict([l.split("=", 1) for l in cookie.split("; ")])
#
# print(cookies)

import requests

headers = {
    # ':authority': 'weibo.cn',
    # ':method': 'GET',
    # ':path': '/',
    # ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': '_T_WM=15676460302; SSOLoginState=1584721288; SCF=AqiOrjk4aSvbMg4JYcHZsIRRBZUe0PjQZiWoqklRniOlOkil89IOXY979N2j6UUiaNqxO-4TF_EL65A4B8S7dMo.; SUB=_2A25zcJ3YDeRhGeBH6FAU9ybJwz2IHXVQmiOQrDV6PUJbktANLRKtkW1NQdzc1Hb9TDQSYg9NFhe8bPzdQfEDYs0S; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF8I8fT-HyNSg6Y5_vfXy0O5JpX5KzhUgL.Foq4e0zfS0nf1h22dJLoIEMLxK-LB--L1h.LxKnL12zLBK-LxKqL1-2L1KqLxK.L1KnLBoSkCXYt; SUHB=0HTxpXubudjLDx; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D20000174',
    'dnt': '1',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
}

response = requests.get(url='https://weibo.cn/', headers=headers)
print(response.status_code)
