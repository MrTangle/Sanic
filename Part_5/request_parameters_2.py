import sanic

app = sanic.Sanic("RequestParameters2")


@app.route("/")
async def index(request):
    print(dir(request))
    return sanic.response.text("OK")


@app.route("/url")
async def index_url(request):
    return sanic.response.text("The url was: {}".format(request.url))


@app.route("/qstring")
async def index_qstring(request):
    return sanic.response.text("The query string was: {}".format(request.query_string))


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080)