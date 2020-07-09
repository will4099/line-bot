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
        r = '帥大真的好愛小Q喔'
    elif msg in ['啾', '啾啾','啾啾啾']:
        r = '啾啾啾啾啾'
    elif '想你' in msg:
        r = '帥大也是，好想好想小Q喔'
    elif msg == '小Q很可愛對吧':
        r = '帥大的小Q最可愛了'
    elif '晚安' in msg:
        r = '晚安我的寶貝公主Q'
    elif '早安' in msg:
        r = '早安小Q'
    elif '加油' in msg:
        r = '啾啾啾，小Q加油'
    elif '臭' in msg:
        r = '你臭Q'
    elif '帥' in msg:
        sticker_message = StickerSendMessage(
            package_id='1',
            sticker_id='5'
        )
    elif msg in ['嗨', '哈囉', '你好', 'hi', 'hello']:
        sticker_message = StickerSendMessage(
            package_id='11537',
            sticker_id='52002738'
        )
    elif '抱抱' in msg:
        sticker_message = StickerSendMessage(
            package_id='11539',
            sticker_id='52114111'
        )


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))  
    line_bot_api.reply_message(
    event.reply_token,
    sticker_message)

           
if __name__ == "__main__":
    app.run()
