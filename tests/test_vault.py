import pytest
from secret_agent_logic import map_secure_command

mapping = {
    "DECRYPT": "openssl decrypt",
    "ENCRYPT": "openssl decrypt",
    "EMPTY": ""
}

def test_valid():
    assert map_secure_command("DECRYPT", mapping) == "openssl decrypt"

def test_type_error():
    with pytest.raises(TypeError):
        map_secure_command(123, mapping)

def test_key_error():
    with pytest.raises(KeyError):
        map_secure_command("GHOST", mapping)

def test_value_error():
    with pytest.raises(ValueError):
        map_secure_command("EMPTY", mapping)