from quart import Quart, request, url_for, redirect, send_file
import requests
import localApi as generator

app = Quart(__name__)

@app.route('/')
async def index():
    return await redirect("https://ruthenic.com") # TODO: redirect to website for this project

@app.route('/api/generate', methods=['POST'])
async def generate():
    data = await request.get_json(force=True)
    print(data)
    phrase = generator.generateRandomPhrase(data["community"])
    return {"phrase": phrase, "community": data["community"]}