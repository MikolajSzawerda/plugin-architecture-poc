from .base import DatasetPlugin

class Plugin2(DatasetPlugin):
    name = "plugin_2"

    def __init__(self, max_rows:int, **kwargs):
        self.max_rows = max_rows

    def load(self, split: str, **kw):
        return [
            f"<Plugin 2: {split}> {i} sentence" for i in range(self.max_rows)
        ]
