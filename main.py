import importlib.metadata as im
from plugins.base import DatasetPlugin
import hydra
from omegaconf import DictConfig, OmegaConf

PLUGIN_REGISTRY = {
        ep.name: ep.load()
        for ep in im.entry_points(group="ds_plugins")
    }

def instantiate_plugin(row: DictConfig) -> DatasetPlugin:
    row_dict = OmegaConf.to_container(row, resolve=True)
    name      = row_dict.pop("name")
    try:
        cls = PLUGIN_REGISTRY[name]
    except KeyError as e:
        raise ValueError(f"Unknown dataset plug‑in: {name}") from e
    return cls(**row_dict)

@hydra.main(config_path="conf", config_name="config", version_base=None)
def main(cfg: DictConfig):
    datasets = []
    for ds_cfg in cfg.datasets:
        plugin = instantiate_plugin(ds_cfg)
        ds = plugin.prepare(ds_cfg['split'])
        datasets.append(ds)
    print(datasets)

if __name__ == "__main__":
    main()