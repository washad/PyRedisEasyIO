import dominate

from pyrediseasyio.io.single_io import SingleIO
from pyrediseasyio.io.boolean_io import BooleanIO
from dominate.tags import div, tr, td, button


class HTMLIO:

    def __init__(self, io: SingleIO):
        key = io.key
        self.io = io
        self.container_id = f'{key}_io'
        self.value_id = f'{key}'
        self.name = io.name
        self.value = io.value
        self.units = io.units
        self.namespace = io.namespace

    def build(self, row_tag: dominate.tags, cell_tag: dominate.tags,
              show_units: bool, show_set: bool, show_reset: bool,
              set_text: str, reset_text: str):
        io = self.io
        name, addr, val, units, ns = io.name, io.addr, io.value, io.units, self.namespace
        show_on_btn = show_set and type(io) == BooleanIO
        show_off_btn = show_reset and type(io) == BooleanIO
        with row_tag(cls=f'easyio_io', id=self.container_id, data_type=type(io).__name__) as container:
            cell_tag(name, cls=f'easyio_name')
            cell_tag(val, cls=f'easyio_value', id=self.value_id, onchange='OnEasyIOValueChange(event)',
                data_namespace=ns, data_addr=addr)

            if show_units:
                units = '' if units is None else units
                cell_tag(units, cls=f'easyio_units')

            if show_on_btn:
                with cell_tag(cls='easyio_btn_cell'):
                    self.set_button(button, set_text)
            elif show_set:
                cell_tag(cls='easyio_btn_cell')

            if show_off_btn:
                with cell_tag(cls='easyio_btn_cell'):
                    self.reset_button(button, reset_text)
            elif show_reset:
                cell_tag(cls='easyio_btn_cell')

        return container


    def set_button(self, tag: dominate.tags = button, txt: str = "On"):
        io = self.io
        name, addr, val, units, ns = io.name, io.addr, io.value, io.units, self.namespace
        ns = "na" if not ns else ns
        tag(txt, cls='easyio_set', onclick=f"EasyIOSet('{ns}','{addr}','{self.value_id}')")


    def reset_button(self, tag: dominate.tags = button, txt: str = "Off"):
        io = self.io
        name, addr, val, units, ns = io.name, io.addr, io.value, io.units, self.namespace
        ns = "na" if not ns else ns
        tag(txt, cls='easyio_reset', onclick=f"EasyIOReset('{ns}','{addr}','{self.value_id}')")


    def html(self, show_units: bool = False, show_set: bool = False, show_reset: bool = False,
              set_text: str = "On", reset_text: str = "Off"):
        """ A wrapper around the 'build' method, using divs for tags"""
        return self.build(div, div, show_units, show_set, show_reset, set_text, reset_text)


    def html_row(self, show_units: bool = False, show_set: bool = False, show_reset: bool = False,
              set_text: str = "On", reset_text: str = "Off"):
        """ A wrapper around the 'build' method, using table elements for tags"""
        return self.build(tr, td, show_units, show_set, show_reset, set_text, reset_text)









