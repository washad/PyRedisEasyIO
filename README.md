# PyRedisEasyIO
A project to simplify reading/writing single objects from/to redis


## Description
Redis is a great way to share data between applications - or processes in an application. 
However, in its raw form, the application has to deal with data type conversion to/from
string, check for existence, and other pesky stuff. It would be nice if that were 
abstracted in such a way to where it didn't appear in code that redis was being used
at all. 

This project seeks to allow the exchange of single data points in a readable way, eg. 
my_data.my_value = 30 (automatically writes '30' to redis) 

## Installation
pip install pyrediseasyio


## Usage
The basis of functionality is the IOGroup class. It acts as a container for individual values
and performs the behind-the-scenes reads and writes. 

~~~~
from io_group import IOGroup
from single_io import BooleanIO, IntIO, FloatIO


class TestGroup1(IOGroup):
    Bool1 = BooleanIO("Boolean 1", "Bool1", False)
    Bool2 = BooleanIO("Boolean 2", "Bool2", True)
    Int1 = IntIO("Integer 1", "Int1")
    Int2 = IntIO("Integer 2", "Int2", default=34)
    MyFloat1 = FloatIO("Float 1", "Float1", default=1.2)

class TestGroup2(IOGroup):
    Bool1 = BooleanIO("Boolean 1", "Bool1", False)
    Bool2 = BooleanIO("Boolean 2", "Bool2", True)
    Int1 = IntIO("Integer 1", "Int1")
    Int2 = IntIO("Integer 2", "Int2", default=34)
    Float1 = FloatIO("Float 1", "Float1", default=1.2)
   

group1a = TestGroup1()
group1b = TestGroup1()
group2 = TestGroup2()

group1a.MyFloat1 = 1234.5         # Performs redis 'set', sending 1234.5 with key 'Float1'
print(group1b.Float1.value)       # Performs redis 'get', calling 'value' converts to primitive type
print(group2.Float1.value)
~~~~

### HTML: 
For convenience, methods are provided to automatically generate html. The 
[dominate](https://github.com/Knio/dominate/blob/master/tests/test_html.py) library is used behind the scenes,
giving you first class access to manipulate the html response; Below is an example of usage, 
consult the test cases for further examples. 

~~~~

class TestGroup(IOGroup):
    Bool1 = BooleanIO("Boolean 1", "Bool1", units="On/Off")
    Float1 = FloatIO("Float 1", "Float1", default=1.23, units="furlongs")


h = HMTLIOGroup(test_group, "my_id", "my_namespace").html().render()
print(h)  #-> Gives;

'''
<div class="my_namespace_io_container" id="my_id_io_container">
  <div class="my_namespace_io" id="my_id_Bool1_io">
    <div class="my_namespace_io_name">Boolean 1</div>
    <div class="my_namespace_io_value" id="my_id_Bool1_io_value" onchange="OnIOValueChange(event)">False</div>
    <div class="my_namespace_io_units">On/Off</div>
  </div>
  <div class="my_namespace_io" id="my_id_Float1_io">
    <div class="my_namespace_io_name">Float 1</div>
    <div class="my_namespace_io_value" id="my_id_Float1_io_value" onchange="OnIOValueChange(event)">1.23</div>
    <div class="my_namespace_io_units">furlongs</div>
  </div>
</div>
'''
        
~~~~
