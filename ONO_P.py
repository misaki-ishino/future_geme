import pandas as pd
import requests
import json

# --- 設定：先ほど作成したURLをここに反映しました ---
DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1479826075033800854/hgYhKoksLjCCfdGUbhRQSewjpkRSBe1hfuyBA_c_fiPx7P9iGpalvAfxNGqYu-rimz1C'

# 小野大輔さんの2026年出演スケジュールデータ
ono_d_data = [
    {"日付": "2026-03-14", "タイトル": "悪魔入りました！入間くん 第4シリーズ イベント", "内容": "WELCOME PARTY!!!!!!"},
    {"日付": "2026-03-15", "タイトル": "戯曲音劇『銀河鉄道の夜』再演", "内容": "朗読劇出演"},
    {"日付": "2026-03-28", "タイトル": "VOICARION 10周年記念公演『スプーンの盾』", "内容": "朗読劇（博多座）"},
    {"日付": "2026-03-29", "タイトル": "AnimeJapan 2026『二十世紀電氣目録』", "内容": "スペシャルステージ"},
    {"日付": "2026-04-05", "タイトル": "劇場版『風都探偵 仮面ライダースカルの肖像』", "内容": "テレビ放送（東映チャンネル）"},
    {"日付": "2026-07-XX", "タイトル": "TVアニメ『二十世紀電氣目録』", "内容": "放送開始（坂本清六 役）"},
]

def create_excel_and_notify():
    # 1. エクセルファイルの作成
    df = pd.DataFrame(ono_d_data)
    file_name = "OnoD_Schedule_2026.xlsx"
    df.to_excel(file_name, index=False)
    
    # 2. Discordへの通知メッセージ作成
    message = (
        f"🔔 **小野大輔さんの出演情報リストを更新しました！**\n"
        f"パソコン内に最新のエクセルファイル（{file_name}）を作成しました。\n\n"
        f"**直近のピックアップ:**\n"
        f"・{ono_d_data[0]['日付']}：{ono_d_data[0]['タイトル']}\n"
        f"・{ono_d_data[1]['日付']}：{ono_d_data[1]['タイトル']}"
    )

    # 3. Discordへ送信
    payload = {"content": message}
    headers = {'Content-Type': 'application/json'}
    
    requests.post(DISCORD_WEBHOOK_URL, data=json.dumps(payload), headers=headers)
    print("Excel作成とDiscord通知が完了しました！")

if __name__ == "__main__":
    create_excel_and_notify()