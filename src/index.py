from hensk import Hensk

app = Hensk()

app.build("127.0.0.1", 8888)

@app.route("/")
@app.route("/test")
def index(request):
    return "Hello, World!" + str(request["query_string"])

@app.route("/asd")
def asd(request):
    return "This is asd page."

app.run()