class MyDict(dict):
    def get(self, key, default=0):
        return super(MyDict, self).get(key, default)


my_dictionary = MyDict({'favourite': 2, 'another': 3, 'last': 4})
print(my_dictionary.get('previous'))
