from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
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
    if '帥' in msg :
        sticker_message = StickerSendMessage(
            package_id='1',
            sticker_id='5'
        )

        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
    else if '嗨' or '哈囉' or '你好' or 'hi' or 'hello' in msg:
        r = '嗨'  
    else if '啾' in msg:
        r = '啾啾啾啾啾'
    else if '愛' in msg:
        r = '最愛小Q了'
    else:
        r = '黎黎不懂'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))
    

if __name__ == "__main__":
    app.run()
