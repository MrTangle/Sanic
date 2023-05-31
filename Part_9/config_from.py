import sanic

app = sanic.Sanic("Config")

# from_envvar ya no existe, habría que confiurar el enviroment de otra forma (con otra biblioteca)
app.config.from_envvar("MY_CONFIG")


@app.route("/<parameter>")
async def index(request, parameter):
    return sanic.response.text("The value of parameter: {}, is {}".format(parameter, app.config.get(parameter, "N.A.")))


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080)