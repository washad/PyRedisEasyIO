from abstract_reader_writer import AbstractReaderWriter
import threading
from errors import PyRedisEasyIOReadOnlyError
from str2bool import str2bool

lock = threading.Lock()


class SingleIO:
    def __init__(self, name: str, addr: str, default: object, reader: AbstractReaderWriter = None):
        self.name = name
        self.addr = addr
        self._reader_writer = reader
        self._value = default

    def __eq__(self, other):
        if isinstance(other, SingleIO):
            other = other.value
        return self.value == other

    def __ne__(self, other):
        if isinstance(other, SingleIO):
            other = other.value
        return self.value != other

    def __get__(self, instance, owner):
        self.read()
        return self

    def __set__(self, obj, value):
        self.write(value)

    def __str__(self):
        return f'[{type(self).__name__}] {self.name} = {self.value}'

    @property
    def value(self):
        return self._convert_type(self._value)

    @staticmethod
    def _convert_type(value):
        return value

    def read(self):
        if self._reader_writer is None:
            return None
        with lock:
            val = self._reader_writer.read(self.addr)
            val = self._convert_type(val)
            self._value = val
            return val

    def write(self, value):
        if self._reader_writer is None:
            return
        with lock:
            value = self._convert_type(value)
            self._reader_writer.write(self.addr, self._convert_type(value))
            self._value = value


class BooleanIO(SingleIO):
    def __init__(self, name: str, addr: str, default: bool = False, reader: AbstractReaderWriter = None):
        super().__init__(name, addr, default, reader)

    @staticmethod
    def _convert_type(value):
        if isinstance(value, str):
            return str2bool(value)
        return bool(value)

    def __bool__(self):
        return self.value
    
    @property
    def value(self) -> bool:
        return super().value


class IntIO(SingleIO):
    def __init__(self, name: str, addr: str, default: bool = False, reader: AbstractReaderWriter = None):
        super().__init__(name, addr, default, reader)

    @staticmethod
    def _convert_type(value):
        return int(value)


class FloatIO(SingleIO):
    def __init__(self, name: str, addr: str, default: bool = False, reader: AbstractReaderWriter = None):
        super().__init__(name, addr, default, reader)

    @staticmethod
    def _convert_type(value):
        return float(value)


class StringIO(SingleIO):
    def __init__(self, name: str, addr: str, default: bool = False, reader: AbstractReaderWriter = None):
        super().__init__(name, addr, default, reader)

    @staticmethod
    def _convert_type(value):
        return str(value)


