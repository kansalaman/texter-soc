import http.client,urllib.request,urllib.parse,urllib.error,json, base64
headers={
'Content-Type':'application/json',
'Ocp-Apim-Subscription-Key':''
}
params=urllib.parse.urlencode({})
conn=http.client.HTTPSConnection('southeastasia.api.cognitive.microsoft.com')
fhand=open('demotext.txt')
lst_of_words=[]
for line in fhand:
    if len(line)<1:
        break
    rbody={
    'documents':[{
    'language':'en',
    'id':'1',
    'text':line
    }]}
    conn.request("POST","/text/analytics/v2.0/keyPhrases?%s" % params,json.dumps(rbody),headers)
    response=conn.getresponse()
    data=response.read().decode()
    resultdic=json.loads(data)
    print(resultdic)
    if(resultdic['errors']==[]):
        lst_of_words.extend(resultdic['documents'][0]['keyPhrases'])
    else:
        continue
print(lst_of_words)
conn.close()
