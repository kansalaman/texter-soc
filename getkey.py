import http.client,urllib.request,urllib.parse,urllib.error,json, base64
headers={
'Content-Type':'application/json',
'Ocp-Apim-Subscription-Key':'d80ae700fdba4e839e7b209bb82ec100'
}
params=urllib.parse.urlencode({})
conn=http.client.HTTPSConnection('southeastasia.api.cognitive.microsoft.com')
fhand=open('demotext.txt')
for line in fhand:
    if len(line)<1:
        break
    rbody='''{
    'documents':[{
    'language':'en',
    'id':'1',
    'text':line
    }]}'''
    conn.request("POST","/text/analytics/v2.0/keyPhrases?%s" % params,rbody,headers)
    response=conn.getresponse()
    data=response.read().decode()
    resultdic=json.loads(data)
    print(resultdic)
conn.close()
