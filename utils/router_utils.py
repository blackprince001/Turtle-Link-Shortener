import secrets
from string import ascii_letters as letters, digits

def rand_char() -> str:
    return secrets.choice(letters + digits)


def generate_keys(custom: str = ""):
    if custom == " " or custom == "":
        key = "".join(rand_char() for _ in range(3)) + "-" + "".join(
            rand_char() for _ in range(3)
        ) + "-" + "".join(rand_char() for _ in range(3))
        custom = key
        
    secret_key = "".join(rand_char() for _ in range(16))
    return (custom, secret_key)