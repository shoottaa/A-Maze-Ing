import sys


REQUIRED_KEYS = {
    "WIDTH",
    "HEIGHT",
    "ENTRY",
    "EXIT",
    "OUTPUT_FILE",
    "PERFECT",
}


def parse_config(file_path: str) -> dict:
    config = {}

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            if "=" not in line:
                print(f"Error : invalid line : '{line}'")
                sys.exit(1)
            key, _, value = line.partition("=")
            config[key.strip()] = value.strip()

    missing = REQUIRED_KEYS - config.keys()
    if missing:
        print(f"Error : missing keys : {', '.join(missing)}")
        sys.exit(1)

    return config
