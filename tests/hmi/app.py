from flask import Flask, Response
from pyrediseasyio import IOGroup, HMTLIOGroup
from pyrediseasyio import StringIO, BooleanIO, FloatIO, IntIO
from dominate.tags import head, script, body, link, div
import dominate


app = Flask(__name__)


class TestGroup(IOGroup):
    FirstName = StringIO("First Name", default="Steve")
    LastName = StringIO("Last Name", default="Jackson")
    Age = IntIO("Age", default=48, units="years")
    IsProgrammer = BooleanIO("Is a programmer", on_value="Yes", off_value="No", default=True)
    IsFather = BooleanIO("Is a father", on_value="Definately", off_value="Not yet", default=True)

test_group = TestGroup()
html_test_group =HMTLIOGroup(test_group)


doc = dominate.document(title='Test Page')
with doc.head:
    link(rel='stylesheet', href='https://www.w3schools.com/w3css/4/w3.css')
    link(rel='stylesheet', href="/static/app.css")
    script(type='text/javascript', src='https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js')
with doc.body:
    with div(cls="w3-card w3-margin w3-border w3-padding"):
        html_test_group.html_table(
            headers=["ITEM", "VALUE", "UNITS"],
            show_set_reset=True)

        with div(cls="w3-card w3-margin w3-border w3-padding"):
            html_test_group.html(
                show_set_reset=True)




@app.route('/')
def hello_world():
    html = doc.render()
    return Response(html)



if __name__ == '__main__':
   app.run(debug=True)