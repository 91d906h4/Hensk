import json
from hensk import Hensk

app = Hensk()

app.build("127.0.0.1", 8888)

@app.route("/")
@app.route("/test")
def index(request):
    return "Hello, World!" + str(request["query_string"])

@app.route("/asd", content_type="json")
def asd(request):
    query_string = request["query_string"]

    return {
        "asdasd": 0
    }

@app.route("/asd", content_type="json", method="POST")
def test(request):

    return json.loads(request["content"])

app.run()