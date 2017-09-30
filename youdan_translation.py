import urllib.request
import urllib.parse
import json
 
while True:
    count = input("请输入你要翻译的内容：(输入(tc)退出程序)\n待翻译的：")
    if count == "tc":
        break
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
    data = {}
    data['i'] = count
    data['type'] = 'AUTO'
    data['from'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_ENTER'
    data['typoResult'] = 'true'
 
    data = urllib.parse.urlencode(data).encode('utf-8')
    resu = urllib.request.urlopen(url,data)
    html = resu.read().decode('utf-8')
    html = json.loads(html)
    #print(html) json形式的数据
    print('\n')
    print('翻译结果：'+ html['translateResult'][0][0]['tgt'] + '\n')
    #print(len(html['smartResult']['entries']))  #翻译的词性长度
    nu = int(len(html['smartResult']['entries']))
    print('其他结果：')
    for each in range(0,nu):
        print(html['smartResult']['entries'][each])
    print('\n'+'翻译结束，执行下一条翻译命令')
    print('********************结束标示********************'+'\n')
