from quart import Quart, redirect, request
from quart_cors import cors

import localApi as generator

app = Quart(__name__)
app = cors(app, allow_origin="*")


@app.route("/")
async def index():
    return await redirect(
        "https://ruthenic.com"
    )  # TODO: redirect to website for this project


@app.route("/api/generate", methods=["POST"])
async def generate():
    data = await request.get_json(force=True)
    print(data)
    phrase = generator.generateRandomPhrase(data["community"])
    return {"phrase": phrase, "community": data["community"]}
