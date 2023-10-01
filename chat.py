from dotenv import load_dotenv
import os
import openai
import random
load_dotenv()
API_KEY = os.getenv('API_KEY')

def random_response():
    responses = [
        '私はランダムに応答するチャットボットです',
        '本当はここにopenAIのAPIを利用したいです',
        'クレカが止まっているのでAPIを動かせませんでした；；',
        'Flask-SocketIOでリアルタイムに情報を反映しています'
    ]
    return responses[random.randint(0, len(responses)-1)]

if __name__ == "__main__":
    print(API_KEY)