from quart import Quart, request, url_for, redirect, send_file
from quart_cors import cors, route_cors
import requests
import localApi as generator

app = Quart(__name__)
app = cors(app, allow_origin="*")

@app.route('/')
async def index():
    return await redirect("https://ruthenic.com") # TODO: redirect to website for this project

@app.route('/api/generate', methods=['POST'])
async def generate():
    data = await request.get_json(force=True)
    print(data)
    phrase = generator.generateRandomPhrase(data["community"])
    return {"phrase": phrase, "community": data["community"]}
