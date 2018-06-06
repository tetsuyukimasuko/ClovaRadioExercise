from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

from flask import Flask
from flask import request
from flask import make_response, jsonify


# Flask app should start in global layout
app = Flask(__name__)


def ResponseForLaunchRequest():
    result={
                "version": "0.1.0",
                "sessionAttributes": {},
                "response": {
                    "outputSpeech": {
                        "type": "SimpleSpeech",
                        "values": [
                            {
                            "type": "PlainText",
                            "lang": "ja",
                            "value": "わかりました。ラジオ体操を流します。"
                            },
                            {
                            "type": "URL",
                            "lang": "" ,
                            "value": "https://change-jp.box.com/shared/static/uiyqhfkdap37z3ocowey07lpfa4sq86b.mp3"
                            }
                        ]
                        },
                    "card": {},
                    "directives": [],
                    "shouldEndSession": True
                    }
                }

    return result


def ResponseForEndRequest():
    result={
                "version": "0.1.0",
                "sessionAttributes": {},
                "response": {
                    "outputSpeech": {
                        "type": "SimpleSpeech",
                        "values": [
                            {
                            "type": "PlainText",
                            "lang": "ja",
                            "value": "わかりました。ラジオ体操を流します。"
                            },
                            {
                            "type": "URL",
                            "lang": "" ,
                            "value": "https://change-jp.box.com/shared/static/uiyqhfkdap37z3ocowey07lpfa4sq86b.mp3"
                            }
                        ]
                        },
                    "card": {},
                    "directives": [],
                    "shouldEndSession": False
                    }
                }
    return result

@app.route('/webhook', methods=['POST'])
def webhook():

    #json解析
    req = request.get_json(silent=True, force=True)
    type=req.get('request')
    type=type.get('type')

    if type=='LaunchRequest':
        result=ResponseForLaunchRequest()
    else:
        pass

    #Clovaに返す
    r = make_response(jsonify(result))
    r.headers['Content-Type'] = 'application/json'
    
    return r


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')
