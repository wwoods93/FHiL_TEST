


class SingletonMeta(type):
    _instances = {}

    def __call__(class_, *args, **kwargs):

        if class_ not in class_._instances:
            print(f"created new instance of {class_}")
            class_._instances[class_] = super().__call__(*args, **kwargs)
        else:
            print("instance {class_} already exists".format(class_=class_))

        return class_._instances[class_]
