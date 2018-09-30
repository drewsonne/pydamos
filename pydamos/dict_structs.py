import inspect


def convert_dict_to_object(cls, struct, _c):
    attrs = get_class_attributes(cls)
    if cls in [float, str, int] or (len(attrs) == 1):
        return cls(struct)
    else:
        response = cls()
        for attr_name, attr_type in attrs:
            if attr_name in struct:
                obj = struct[attr_name]
                if attr_name == 'geopoint':
                    obj = obj[0].split(',')
                attr_value = obj
                if type(attr_type) == list:
                    result_structure = []
                    attr_type = attr_type[0]
                    for element in obj:
                        result_structure.append(
                            convert_dict_to_object(
                                attr_type, element, _c
                            )
                        )
                    attr_value = result_structure
                elif type(attr_type) == dict:
                    dict_types = list(attr_type.items()).pop()
                    attr_dict_key_type = dict_types[0]
                    attr_dict_value_type = dict_types[1]
                    result_structure = {}
                    for key, value in obj.items():
                        key = attr_dict_key_type(key)
                        result_structure[key] = convert_dict_to_object(
                            attr_dict_value_type, value, _c
                        )
                    attr_value = result_structure
                setattr(response, attr_name, attr_value)
            else:
                if attr_name != '_c':
                    if hasattr(response, attr_name):
                        delattr(response, attr_name)

    response._c = _c

    return response


def get_class_attributes(cls):
    attributes = inspect.getmembers(cls, lambda a: not (inspect.isroutine(a)))
    return [a for a in attributes if not (a[0].startswith('__') and a[0].endswith('__'))]
