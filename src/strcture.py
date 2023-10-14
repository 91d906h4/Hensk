# Import modules.
from typing import Callable

# RouteIndex structure.
class RouteIndex():
    def __init__(self, method: str, content_type: str, func: Callable) -> None:
        self.method = method
        self.type = content_type
        self.func = func