
class FileStorage:
    __file_path = "file.json"
    __objects = {}
    def all(self):
        return self.__file_path
    def new(self, obj):
        key = type(obj).__name__ + "." + obj.id
        self.__objects[key] = obj.__dict__
        return self.__objects