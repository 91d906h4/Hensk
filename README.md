# Hensk

A simple back-end framework build with Python.

# Usage

This is a very simple Hensk application.

```py
from hensk import Hensk

app = Hensk()

app.build("127.0.0.1", 8888)

@app.route("/")
def index(request):
    return "Hello, World!"

app.run()
```

Basically, you can use Hensk just like Flask, but Hensk only support some very simple function. Hensk is aim help user create an API server faster.

Here is a simple API server build with Hensk. This API can calculate `+`, `-`, `*`, and `/`.

```py
from hensk import Hensk

app = Hensk()

app.build("127.0.0.1", 8888)

@app.route("/add", method="GET", content_type="json")
def index(request):
    a = int(request["query_string"]["a"])
    b = int(request["query_string"]["b"])

    return {
        "result": a + b
    }

@app.route("/sub", method="GET", content_type="json")
def index(request):
    a = int(request["query_string"]["a"])
    b = int(request["query_string"]["b"])

    return {
        "result": a - b
    }

@app.route("/mul", method="GET", content_type="json")
def index(request):
    a = int(request["query_string"]["a"])
    b = int(request["query_string"]["b"])

    return {
        "result": a * b
    }

@app.route("/div", method="GET", content_type="json")
def index(request):
    a = int(request["query_string"]["a"])
    b = int(request["query_string"]["b"])

    return {
        "result": a / b
    }

app.run()
```

Now, you can just use you browser to access http://127.0.0.1:8888/add?a=1&b=2, and you will see the result 3 on the screen.