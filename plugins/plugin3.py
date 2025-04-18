from .base import DatasetPlugin

class Plugin3(DatasetPlugin):
    name = "plugin_3"

    def __init__(self, max_rows:int, postfix: str, **kwargs):
        self.max_rows, self.postfix = max_rows, postfix

    def load(self, split: str, **kw):
        return [
            f"<Plugin 3: {split}> {i} sentence {self.postfix}" for i in range(self.max_rows)
        ]
