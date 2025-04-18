from .base import DatasetPlugin

class Plugin1(DatasetPlugin):
    name = "plugin_1"

    def __init__(self, max_rows:int, expand: bool=False, **kwargs):
        self.max_rows, self.expand = max_rows, expand

    def load(self, split: str, **kw):
        return [
            f"<Plugin 1: {split}> {i} sentence {'expanded' if self.expand else ''}" for i in range(self.max_rows)
        ]
