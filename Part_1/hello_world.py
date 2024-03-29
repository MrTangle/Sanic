import sanic

app = sanic.Sanic(name="HelloWorld")


@app.route("/", name="root")
async def index(request):
    return sanic.response.text("Got GET request on default root: Hello World!")


@app.route("/json", name="json")
async def json(request):
    return sanic.response.json({"Hello": "World"})


@app.route("/debug", name="debug")
async def json(request):
    raise ValueError("Woot!")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
