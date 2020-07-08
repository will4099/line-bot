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
    r = '黎黎不懂'
    if '愛' in msg:
        r = '最愛小Q了'
    elif '啾啾啾啾' in msg:
        line_bot_api.reply_message(
            event.reply_token,
            StickerSendMessage(
                package_id='11538',
                sticker_id='51626495'
            ))
        r = '帥大真的好愛小Q喔'
    elif msg == '啾' or '啾啾' or '啾啾啾' :
        r = '啾啾啾啾啾'
        return

    if '想你' in msg:
        r = '帥大也是，好想好想小Q喔'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))

    elif '帥' in msg :
        line_bot_api.reply_message(
            event.reply_token,
            StickerSendMessage(
                package_id='1',
                sticker_id='5'
            ))
    elif msg in ['嗨', '哈囉', '你好', 'hi', 'hello']:
        line_bot_api.reply_message(
            event.reply_token,
            StickerSendMessage(
                package_id='11537',
                sticker_id='52002738'
            ))
        return

    if '抱抱' in msg:
        line_bot_api.reply_message(
            event.reply_token,
            StickerSendMessage(
                package_id='11539',
                sticker_id='52114111'
            ))


if __name__ == "__main__":
    app.run()
