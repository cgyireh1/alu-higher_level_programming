#!/usr/bin/python3
"""defines Base class"""



class Base():
    """manages id attribute in all future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes to given id or
        increases class nb_objects and sets as default id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation of list of dictionaries"""
        import json
        if list_dictionaries is None:
            return "[]"
        if len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representaiton of
        list of instances who inherits from Base to a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        list_dictionaries = []
        for instance in list_objs:
            list_dictionaries.append(instance.to_dictionary())
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation
        for list of dictionaries"""
        import json
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        using update method"""
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1, 0, 0)
        if cls.__name__ == "Square":
            instance = cls(1, 0, 0)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """return list of instances from file containing saved JSON string"""
        filename = cls.__name__ + ".json"
        results = []
        try:
            with open(filename, 'r') as f:
                for instance in cls.from_json_string(f.read()):
                    results.append(cls.create(**instance))
        except Exception as err:
            pass
        return (results)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes and deserializes in CSV with 
        same behavior as the JSON serialization/deserialization"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                for o in list_objs:
                    if cls.__name__ == "Rectangle":
                        writer.writerow([o.id, o.width, o.height, o.x, o.y])
                    if cls.__name__ == "Square":
                        writer.writerow([o.id, o.size, o.x, o.y])

                        @classmethod
                        def load_from_file_csv(cls):
                            """Serializes and deserializes in CSV with same behavior as the JSON"""
                            objs = []
                            filename = cls.__name__ + ".csv"
                            try:
                                with open(filename, 'r', newline='') as f:
                                    reader = csv.reader(f)
                                    for row in reader:
                                        if cls.__name__ == "Rectangle":
                                            dic = {"id": int(row[0]),
                                                    "width": int(row[1]),
                                                    "height": int(row[2]),
                                                    "x": int(row[3]),
                                                    "y": int(row[4])}
                                            if cls.__name__ == "Square":
                                                dic = {"id": int(row[0]),
                                                        "size": int(row[1]),
                                                        "x": int(row[2]),
                                                        "y": int(row[3])}
                                                o = cls.create(**dic)
                                                objs.append(o)
                                    return objs
