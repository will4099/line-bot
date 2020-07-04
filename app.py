<<<<<<< HEAD
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('dvi4+TbHBY3peCO29ldcYeJjRoddEKKrkiX8uWJTSsXITf/e+sTMM/g5MkQ8WNITA0/XgT9j6Kgwx0/sKMEN9azOqD/FBsfRuPYAHrTkeYJtf99O23x7bJtoMiy99y8Ac/Mhl3QqJnbEanuMNI/RLwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('4cf41939cf6e66179069b061b37c4ec6')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = "Wilson doesn't understand what you are saying"
    if "嗨" or '哈囉' or '你好' or 'hi' or 'hello' in msg:
        r = 'Hello'
    if '愛' in msg:
        print('啾啾啾啾啾')
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=))


if __name__ == "__main__":
=======
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('dvi4+TbHBY3peCO29ldcYeJjRoddEKKrkiX8uWJTSsXITf/e+sTMM/g5MkQ8WNITA0/XgT9j6Kgwx0/sKMEN9azOqD/FBsfRuPYAHrTkeYJtf99O23x7bJtoMiy99y8Ac/Mhl3QqJnbEanuMNI/RLwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('4cf41939cf6e66179069b061b37c4ec6')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
>>>>>>> ca9c51d658879fa3e0a3947f3e07db091ae57136
    app.run()