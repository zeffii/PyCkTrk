class CKProperty:
    def __init__(self, **kwargs):
        self.params = kwargs
    def __repr__(self):
        ...
    def __str__(self):
        ...
    def name(self):
        return self.params['name']
    def dots(self):
        if self.params['kind'] == 'hex':
            return '.' * len(self.params['max'])
