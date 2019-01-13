# -*- coding = utf-8 -*-
# -*- author = Jazzzzon -*-
import requests

request = requests.get(r'https://www.baidu.com')
content = request.content
print(content)
