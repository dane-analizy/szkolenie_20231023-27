import yaml

def load_config(config_file = "db_config.yaml"):
    with open(config_file, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return config


def kto_to():
    print(__name__)