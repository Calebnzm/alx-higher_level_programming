#!/usr/bin/python3
"""This is a module to degine the base class"""
import json
import csv


class Base:
    """This is a module to degine the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """this is a constructor for the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON format for a list of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes json to a file"""
        if list_objs is None:
            list_objs = []
        class_name = cls.__name__
        filename = ("{}.json".format(class_name))
        object_list = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(object_list)
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file and return a list"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_str = file.read()
                json_list = cls.from_json_string(json_str)
                instances = [cls.create(**data) for data in json_list]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    id = obj.id
                    writer.writerow([id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r", newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                ob = []
                if cls.__name__ == "Rectangle":
                    for row in reader:
                        x = row[1]
                        y = row[2]
                        z = row[3]
                        a = row[4]
                        b = row[0]
                        ob.append(cls(int(x), int(y), int(z), int(a), int(b)))
                elif cls.__name__ == "Square":
                    for row in reader:
                        c = row[1]
                        d = row[2]
                        e = row[3]
                        g = row[0]
                        ob.append(cls(int(c), int(d), int(e), int(g)))
                return ob
        except FileNotFoundError:
            return []
