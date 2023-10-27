import yaml

with open("db_config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)
