from fastapi import FastAPI, Request
import json
import requests
import os
import streamlit as st

app = FastAPI()

DISCORD_WEBHOOK_URL = st.secrets["DISCORD_WEBHOOK_URL"]

@app.post("/webhook")
async def webhook(request: Request):
    form = await request.form()
    data = json.loads(form['data'])

    # 构建要发送到 Discord 的消息
    message = {
        "content": f"New donation from {data['from_name']}!\n"
                   f"Amount: {data['amount']} {data['currency']}\n"
                   f"Message: {data['message']}"
    }

    # 发送消息到 Discord Webhook
    response = requests.post(DISCORD_WEBHOOK_URL, json=message)

    if response.status_code == 204:
        return {"status": "success"}
    else:
        return {"status": "failed", "detail": response.text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
