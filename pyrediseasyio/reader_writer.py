
import redis
from abstract_reader_writer import AbstractReaderWriter


class ReaderWriter(AbstractReaderWriter):

    def __init__(self, host='localhost', port=6379, db=0):
        self._server = redis.StrictRedis(host=host, port=port, db=db, decode_responses=True)

    def read(self, addr):
        return self._server.get(addr)

    def write(self, addr, value):
        value = str(value)
        self._server.set(addr, value)



