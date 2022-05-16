"""
@author : moshe_arus
@date : 16/05/2022 18:20
"""
import inspect


class diff_tool:
    """
     python module to compare 2 object attribute's

    """

    def __init__(self, old_obj=object, new_obj=object, hash_visit={}, changes=[]):
        """
        :param old_obj: the main obj
        :type old_obj : object
        :param new_obj: the sub obj or diff obj to compare
        :type new_obj : object
        :param hash_visit: memory hashtable to the checked obj
        :type hash_visit: dict
        :param changes: list of change from the first attribute , if attribute has a complex change
        its show in accordance.
        :type changes : list
        """
        self.old_obj = old_obj
        self.new_obj = new_obj
        self.hash_visit = hash_visit
        if changes is None :
            self.changes = []
        else :
            self.changes = changes

    def get_attributes(self, obj):
        """
        the method get an object
        :param obj: object - can be instance or class
        :type obj: object
        :return: list of attributes of this obj
        :rtype list
        """
        attributes = inspect.getmembers(obj, lambda a : not (inspect.isroutine(a)))
        attributes = [a for a in attributes if not (a[0].startswith('__') and a[0].endswith('__'))]
        final_attributes = []
        for item in attributes:
            if item[0]  not in ['denominator','imag','numerator','real']:
                final_attributes.append(item[0])
        return final_attributes

    def diff_objects(self, object_a=object, object_b=object):
        """
        the method find the difference between 2 obj
        can be type , value , complex
        :param object_a: old object
        :type object_a: object
        :param object_b: new_object
        :type object_b: object
        :return: list of all diff changes  accordingly from the start to the end
        :rtype list

        """
        # memory condition to break ;
        if id(object_a) == id(object_b) :
            return 0
        object_a_attrs = self.get_attributes(object_a)
        object_b_attrs = self.get_attributes(object_b)
        len(object_b_attrs)
        # one of the obj has no uncheckd  attirbute anymore
        if len(object_a_attrs) == 0 or len(object_b_attrs) == 0:
            return 0
      
      
        for old_attr, new_attr in zip(object_a_attrs, object_b_attrs) :
            # type case condition
            if type(getattr(object_a, old_attr)) is not type(getattr(object_b, new_attr)) :
                self.changes.append(
                    "Attribute "+old_attr+" type change "+str(type(getattr(object_a, old_attr)))+" -> "+str(
                        type(
                            getattr(object_b, new_attr))))

            # value case condition
            if getattr(object_a, old_attr) is not getattr(object_b, new_attr) and type(
                    getattr(object_a, old_attr)) is type(getattr(object_b, new_attr)) and type(
                getattr(object_a, old_attr)) is (
                    int or float or complex) and type(getattr(object_b, new_attr)) is (int or float or complex) :
                self.changes.append(
                    "Attribute "+old_attr+" value change "+str(getattr(object_a, old_attr))+" -> "+str(
                        getattr(
                            object_b, new_attr)))
            # attribute is object condition => start recursively
            typesTuple = (
                dict, list, int, complex, float, str, tuple, set, range, frozenset, bytes, bytearray, memoryview)
            if not (isinstance(getattr(object_a, old_attr), typesTuple) and isinstance(getattr(object_b, new_attr),
                                                                                       typesTuple)):
                # condition that  object point to  Himself
                if id(getattr(object_a, old_attr)) in self.hash_visit or id(
                        getattr(object_b, new_attr)) in self.hash_visit :
                    pass
                else:
                    self.hash_visit[id(getattr(object_a, old_attr))] = 'visited'
                    self.hash_visit[id(getattr(object_b, new_attr))] = 'visited'
                    self.changes.append('complex change in '+str(old_attr))
                    return self.diff_objects(object_a=getattr(object_a, old_attr), object_b=getattr(object_b, new_attr))
                    self.changes.append('end of prev  complex change')

