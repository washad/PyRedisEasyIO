from reader_writer import ReaderWriter
from single_io import SingleIO
import json


class IOGroup(ReaderWriter):

    def __init__(self, host='localhost', port=6379, db=0):
        super().__init__(host=host, port=port, db=db)
        all_members = [d for d in dir(self) if not d.startswith('__')]
        self.members = []
        for member_name in all_members:
            try:
                attr = getattr(self, member_name)
                if not isinstance(attr, SingleIO):
                    continue
                attr._reader_writer = self
                self.members.append(member_name)
            except AttributeError:
                pass

    def dumps(self):
        members = []
        for m in self.members:
            attr = getattr(self, m)
            members.append(dict(name=attr.name, addr=attr.addr, value=attr.value))
        return json.dumps(members)


