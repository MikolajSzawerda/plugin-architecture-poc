from abc import ABC, abstractmethod

class DatasetPlugin(ABC):
    name: str

    @abstractmethod
    def load(self, split: str, **kw) -> list[str]:           # download/stream
        ...

    def prepare(self, split: str = "train", **kw) -> list[str]:
        """Default pipeline: load ➜ custom row ops ➜ return HF Dataset."""
        ds = self.load(split, **kw)
        return self.apply_transforms(ds)

    # override only if you need per‑dataset transforms
    def apply_transforms(self, ds: list[str]) -> list[str]:
        return ds
