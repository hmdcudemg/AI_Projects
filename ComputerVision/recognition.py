import http.client
import urllib
import base64
import json
import re

# Change {MS_API_KEY} BELOW WHIT YOUR MICROSFOT VISION API KEY
ms_api_key = "{MS_API_KEY}"

# Setup vision API
headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': ms_api_key,
}
params = urllib.parse.urlencode({
    'visualFeatures': 'Description',
})

# read image
body = open('tmp/image1.jpg', "rb").read()

# submit request to API and print description if successfuly or error otherwise
try:
    conn = http.client.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
    response = conn.getresponse()
    analysis = json.loads(response.read())
    #print(analysis)
    image_caption = analysis["description"]["captions"][0]["text"].capitalize()
    conn.close()
    print(image_caption)
except Exception as e:
    print("error, %s" % e)
    e.args
