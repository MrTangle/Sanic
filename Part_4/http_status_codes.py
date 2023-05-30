import sanic
from sanic.exceptions import SanicException

app = sanic.Sanic("HttpStatusCode")


@app.route("/")
async def index(request):
    return sanic.response.text("Welcome to error handling!")


@app.route("/<error_code:int>")
async def error_code(request, error_code):
    raise SanicException("Something gone wrong!", status_code = error_code)


@app.route("/abort/<error_code:int>")
async def abort_error_code(request, error_code):
    sanic.exceptions.abort(error_code)


@app.exception(sanic.exceptions.NotFound)
async  def ignore_404(request, exception):
    return sanic.response.text("Oh no, the page you are looking for: {} does not exist!".format(request.url))


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080)