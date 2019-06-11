

class PyRedisEasyIOReadOnlyError(Exception):
    def __init__(self):
        super().__init__("The IO type cannot be set, it is read only!")


class PyRedisEasyIOAddressNotFoundError(Exception):
    def __init__(self, addr: str):
        super().__init__(f"No IO was found with the address of {addr}!")
