import dominate
from dominate.util import raw

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
            self.html_name_cell(cell_tag)
            self.html_value_cell(cell_tag)

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
        return tag(txt, cls='easyio_set', onclick=f"EasyIOSet('{ns}','{addr}','{self.value_id}')")

    def reset_button(self, tag: dominate.tags = button, txt: str = "Off") -> dominate.tags:
        io = self.io
        name, addr, val, units, ns = io.name, io.addr, io.value, io.units, self.namespace
        ns = "na" if not ns else ns
        return tag(txt, cls='easyio_reset', onclick=f"EasyIOReset('{ns}','{addr}','{self.value_id}')")

    def html(self, show_units: bool = False, show_set: bool = False, show_reset: bool = False,
              set_text: str = "On", reset_text: str = "Off") -> dominate.tags:
        """ A wrapper around the 'build' method, using divs for tags"""
        return self.build(div, div, show_units, show_set, show_reset, set_text, reset_text)

    def html_row(self, show_units: bool = False, show_set: bool = False, show_reset: bool = False,
              set_text: str = "On", reset_text: str = "Off") -> dominate.tags:
        """ A wrapper around the 'build' method, using table elements for tags"""
        return self.build(tr, td, show_units, show_set, show_reset, set_text, reset_text)

    def html_name_cell(self, tag: dominate.tags = div) -> dominate.tags:
        return tag(self.io.name, cls=f'easyio_name')

    def html_value_cell(self, tag: dominate.tags = div) -> dominate.tags:
        """Generate the html for generating the cell that contains the object value."""
        io = self.io
        name, addr, val, units, ns = io.name, io.addr, io.value, io.units, self.namespace
        return tag(val, cls=f'easyio_value', id=self.value_id, onchange='OnEasyIOValueChange(event)',
                 data_namespace=ns, data_addr=addr)

    def html_value_svg_circle(self, x: int, y: int, r: int):
        return raw(f'<circle cls=easyio_value" id="{self.value_id}" cx="{x}" cy="{y}" r="{r}"></circle>')









