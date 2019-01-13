# -*- coding = utf-8 -*-

import re
import requests

request = requests.get(r'https://www.baidu.com')
content = request.content
print(content)
