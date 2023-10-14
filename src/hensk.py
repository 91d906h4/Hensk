# Import modules.
import socket
import threading

from strcture import RouteIndex

class Hensk():
    def __init__(self) -> None:
        self.host = "127.0.0.1"
        self.port = 8080
        self.route_index = {}

    def __socket(self, host: str="127.0.0.1", port: int=8080) -> socket.socket:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((str(host), int(port)))
        server_socket.listen(1)

        return server_socket

    def build(self, host: str, port: int) -> None:
        r"""
        This function is used to change the defualt setting. The following are the settings of Hensk.

        host: The host of server.
        port: The port of server (the port should be a integer).
        """
        if host: self.host = str(host)
        if port: self.port = int(port)

    def __response(self, client_connection: socket.socket, request: str, client_ip: str) -> None:
        request = self.__request_parser(request=request)

        # Set defualt values.
        path            = request["path"]
        method          = request["method"]
        header          = "404 Not Found"
        content_type    = "text/html"
        content         = "404 Not Found."

        # Generate response.
        try:
            # Check if path in reoute_index.
            if path in self.route_index:
                # Check if method matchs.
                if method != self.route_index[path].method:
                    header = "404 Not Found"
                    content = "Page Not Found."

                else:
                    header = "200 OK"
                    content = str(self.route_index[path].func(request))

        # Ignore exceptions.
        except: pass

        # Send HTTP response.

        # Header.
        client_connection.send(f"HTTP/1.1 {header}\n".encode())

        # Content-Type.
        client_connection.send(f"Content-Type: {content_type}\n".encode())

        # Append a new line between header and contents.
        client_connection.send("\n".encode())

        # Contents.
        client_connection.send(content.encode())

        # Close connection.
        client_connection.close()

    def __request_parser(self, request: str) -> dict:
        request = request.split("\n")

        # Set defualt value.
        path            = ""
        method          = ""
        query_string    = ""

        for line in request:
            if line.startswith(("GET", "POST", "POST", "OPTIONS", "PUT", "DELETE", "TRACE", "PATCH", "LINK", "UNLINK")):
                method, path, _ = line.split()

                if "?" in path:
                    path, query_string = path.split("?")

                if "&" in query_string:
                    query_string = query_string.split("&")

                break

        return {
            "path":         path,
            "query_string": query_string,
            "method":       method
        }

    # Set route index.
    def route(self, path: str, method: str = "GET", content_type: str = "html"):
        r"""
        Use the @app.route the route the request. For example:

        @app.route("/", method="GET")
        def index():
            return "Hello, World!"

        This will return a "Hello, World!" string to user while the user access http://127.0.0.1:8080/.
        """

        # Get route function.
        def _route(func):
            self.route_index[path] = RouteIndex(method=method, content_type=content_type, func=func)
            return func

        return _route

    def run(self) -> None:
        print(f"Thank you for using Hensk web application frmaework.")
        print(f"Server start at {self.host}:{self.port}.")

        server_socket = self.__socket(self.host, self.port)

        while True:
            try:
                client_connection, client_address = server_socket.accept()

                request = client_connection.recv(1024).decode()

                threading.Thread(target=self.__response, args=(client_connection, request, client_address[0], )).start()

            except KeyboardInterrupt: break
            except Exception as e: print(str(e))

        server_socket.close()

        print(f"Server shutdown successfully.")

        exit(0)