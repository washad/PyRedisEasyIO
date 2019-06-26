from pyrediseasyio.io.boolean_io import BooleanIO
from pyrediseasyio.io.io_group import IOGroup
from pyrediseasyio.html.html_io import HTMLIO
from typing import List, Callable
from dominate.tags import div, table, tr, th
import dominate
import json


class HMTLIOGroup:

    def __init__(self, io_group: IOGroup):
        self._io_group = io_group
        self.namespace = io_group.namespace


    def _heading(self, headers, row_tag: dominate.tags, cell_tag: dominate.tags):
        if headers:
            with row_tag(cls="easyio_header_row"):
                for h in headers:
                    cell_tag(h, cls="easyio_header_cell")

    def html(self, headers: List[str] = None,
             by_names: List = None,
             by_type: List = None,
             by_lambda_each: Callable = None,
             by_lambda_results: Callable = None,
             show_units: bool = True,
             show_set_reset: bool = False,
             set_text: str = "On",
             reset_text: str = "Off",
             html_id: str = None):

        attrs = self._io_group.get_attributes(by_names, by_type, by_lambda_each, by_lambda_results)
        html_id = f'{attrs[0].key}_io_container' if html_id is None else html_id

        with div(cls=f'easyio_container', id=html_id) as container:
            self._heading(headers, div, div)
            for attr in attrs:
                HTMLIO(attr).html(show_units, show_set_reset, show_set_reset, set_text, reset_text)
        return container



    def html_table(self, headers: List[str] = None,
                   by_names: List = None,
                   by_type: List = None,
                   by_lambda_each: Callable = None,
                   by_lambda_results: Callable = None,
                   show_units: bool = True,
                   show_set_reset: bool = False,
                   set_text: str = "On",
                   reset_text: str = "Off",
                   html_id: str = None):

        attrs = self._io_group.get_attributes(by_names, by_type, by_lambda_each, by_lambda_results)
        html_id = f'{attrs[0].addr}_io_container' if html_id is None else html_id

        with table(cls=f'easyio_container', id=html_id) as container:
            self._heading(headers, tr, th)
            for attr in attrs:
                HTMLIO(attr).html_row(show_units, show_set_reset, show_set_reset, set_text, reset_text)
        return container



    def dumps(self, by_names: List = None, by_type: List = None,
              by_lambda_each: Callable = None, by_lambda_results: Callable = None):

        attrs = self._io_group.get_attributes(by_names, by_type, by_lambda_each, by_lambda_results)

        def f(a):
            io = HTMLIO(a)
            value, display_value = io.value, io.value
            if isinstance(a, BooleanIO):
                display_value = a.on_value if value == True else a.off_value

            return dict(id=io.value_id, name=io.name, value=io.value, units=io.units, display_value=display_value)

        results = [f(a) for a in attrs]

        return json.dumps(results)


