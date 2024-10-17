import typing as _typing


class Dict(dict):
    DUPKEYS = '__dupkeys__'
    OPS = '__ops__'
    MODIFIERS = '__modifiers__'
    """
    a dictionary that can store duplicate keys and their operations and modifiers.

    
    """
    
    
    '''
    the running logic of creating a dictionary:
    1. The Dict instance is created.
    2. The __init__ method is called with the provided iterable.
    3. For each key-value pair in the iterable, self[k] = v is executed.
    4. This assignment triggers the __setitem__ method for each key-value pair.
    5. If __setitem__ is overridden to handle duplicate keys by modifying the key names, this logic is applied here.
    6. Once all key-value pairs have been processed, the __init__ method completes.
    
    '''

    def __init__(self, iterable=()):
        super().__init__()
        for k, v in iterable:
            self[k] = v

    def _get_meta(self, key):
        if key not in self:
            # super().__setitem__(key, {}) is calling the __setitem__ method of the base class (dict in this case) to set the value of the specified key to an empty dictionary {}.
            super().__setitem__(key, {})
        return self[key]
    # The @property decorator in Python is used to define methods in a class that behave like attributes. This allows you to access a method as if it were a simple attribute, without needing to call it with parentheses. 
    @property
    def dupkeys(self) -> _typing.Dict[str, _typing.List[str]]:
        return self._get_meta(self.DUPKEYS)
    # Q why use this property
    # A to store the duplicate keys

    @property
    # In Python's typing module, types are usually represented with capitalized names (e.g., List, Dict, Tuple) to distinguish them from their built-in counterparts (list, dict, tuple). 
    def ops(self) -> _typing.Dict[str, str]:
        return self._get_meta(self.OPS)
    # Q why use this property

    @property
    def modifiers(self) -> _typing.Dict[str, _typing.List[str]]:
        return self._get_meta(self.MODIFIERS)
    # Q why use this property

    def __setitem__(self, key, value):
        '''
        if key is already in the dictionary, append a new key with the same name but with a different index
        
        the new key name is the original key name plus the length of the duplicate keys list in the dictionary['__dupkeys__']
        
        store the operation, modifiers, and value in the dictionary of the new key
        
        
        '''
        # intersing usage of the * operator
        op, *mod, v = value

        if key in self:
            if key not in self.dupkeys:
                self.dupkeys[key] = [key]
            new_key = f'{key}+{len(self.dupkeys[key])}'
            # comment i think this is for the case when the key is already in the dictionary,like the district
            self.dupkeys[key].append(new_key)
            key = new_key

        if op != '=':
            self.ops[key] = op
        # Q don't understand the usage of this if statement

        if mod:
            self.modifiers[key] = mod
        # Q don't understand the usage of this if statement

        return super().__setitem__(key, v)
