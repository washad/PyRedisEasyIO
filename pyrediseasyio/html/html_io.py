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



    def html(self, show_units: bool = True,
             show_set_reset: bool = False,
             set_text: str = "On",
             reset_text: str = "Off"):
        io = self.io
        name, addr, val, units, ns = io.name, io.addr, io.value, io.units, io.namespace
        with div(cls=f'easyio_io', id=self.container_id, data_type=type(io).__name__) as container:
            div(name, cls=f'easyio_name')
            div(val, cls=f'easyio_value', id=self.value_id, onchange='OnEasyIOValueChange(event)',
                data_namespace=ns, data_addr=addr)
            if show_units:
                units = '' if units is None else units
                div(units, cls=f'easyio_units')
            if show_set_reset and type(io) == BooleanIO:
                button(set_text, cls=f'easyio_set',
                       onclick=f'EasyIOSet({ns},{addr},{self.value_id})')
                button(reset_text, cls=f'easyio_reset',
                       onclick=f'EasyIOReset({ns},{addr},{self.value_id})')
        return container



    def html_row(self, show_units: bool = True,
             show_set_reset: bool = False,
             set_text: str = "On",
             reset_text: str = "Off"):
        io = self.io
        name, addr, val, units, ns = io.name, io.addr, io.value, io.units, io.namespace
        with tr(cls=f'easyio_io', id=self.container_id, data_type=type(io).__name__) as container:
            td(name, cls=f'easyio_name')
            td(val, cls=f'easyio_value', id=self.value_id, onchange='OnEasyIOValueChange(event)',
                data_namespace=ns, data_addr=addr)
            if show_units:
                units = '' if units is None else units
                td(units, cls=f'easyio_units')
            if show_set_reset and type(io) == BooleanIO:
                with td():
                    button(set_text, cls=f'easyio_set', style='display: inline-block;',
                           onclick=f'EasyIOSet({ns},{addr},{self.value_id})')
                    button(reset_text, cls=f'easyio_reset', style='display: inline-block;',
                           onclick=f'EasyIOReset({ns},{addr},{self.value_id})')
        return container







