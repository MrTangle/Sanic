import sanic

app = sanic.Sanic("RequestTypes2")

@app.get("/get")
async def get_context(request):
    return sanic.response.text("Hit was with GET!")


@app.post("/post")
async def post_context(request):
    return sanic.response.text("Hit was with POST!")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080)