import logging

logging.basicConfig(
    filename="audit.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def map_secure_command(alias, mapping_dict):
    if not isinstance(alias, str):
        logging.error(f"TypeError: {alias}")
        raise TypeError("Alias must be string")

    try:
        command = mapping_dict[alias]

        if not command:
            logging.error(f"Empty command: {alias}")
            raise ValueError("Empty command")

        return command

    except KeyError:
        logging.error(f"Alias not found: {alias}")
        raise KeyError("Alias not found")