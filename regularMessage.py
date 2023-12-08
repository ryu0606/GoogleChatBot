from google_chat import GoogleChat
from nowTime import NowTime

#現在の時間を取得
time = NowTime
dt_now = time.getNowTime()

# {Webhook URL}を指定してGoogleChatインスタンスを生成
chat = GoogleChat("googlechatのURL")

# テキストメッセージを投稿
chat.postText("*"+ dt_now +"諸連絡*")

# Widgetを投稿
widgets = [
  {
    'textParagraph': { 'text': "<a href='https://www.google.co.jp/'>Google</a>" }
  }
]

print("投稿完了")
