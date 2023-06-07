import hydra
from omegaconf import DictConfig

from oml.lightning.pipelines.predict import extractor_prediction_pipeline


@hydra.main(config_path=".", config_name="predict_sop.yaml")
def main_hydra(cfg: DictConfig) -> None:
    extractor_prediction_pipeline(cfg)


if __name__ == "__main__":
    main_hydra()