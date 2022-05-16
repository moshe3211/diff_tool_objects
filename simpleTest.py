import inspect
from attr import  define
from diff_tool import diff_tool
import collections

"""
some tests to check the diff_toll

"""


@define
class A():
    attr_a: None
    attr_b:None
    attr_c:None
@define
class B():
    attr_c:None



A_instance = A(attr_a=5,     attr_b="dfdf", attr_c=B(attr_c=4))
B_instance = A(attr_a=6,     attr_b =5, attr_c=B(attr_c='sg'))
dif= diff_tool(A_instance,B_instance)
dif.diff_objects(dif.old_obj,dif.new_obj)
print("""should be => 
attr_a value -> 6 
attr_b type change str -> int 
attr_c  complex change : 
attr_c type change -> str
""")
print('result =>')
[print(x) for x in dif.changes]
