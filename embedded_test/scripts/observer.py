


class ObservableAbstract:

    def __init__(self, name):
        self.name = name
        self._observers = []

    def attach(self, observer):
        """attach observer"""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """detach observer"""
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message, message_type=None):
        """notify all attached observers"""
        for observer in self._observers:
            observer.update(message, message_type)


class ObservableBasic(ObservableAbstract):

    def __init__(self, name):
        super().__init__(name)




class ObserverAbstract:

    def __init__(self, name):
        self._name = name

    def update(self, message, message_type=None):
        raise NotImplementedError("subclass must implement update()")


class ObserverBasic(ObserverAbstract):
    def __init__(self, name):
        super().__init__(name)

    def update(self, message, message_type=None):
        print("{name} received: {message}".format(name=self._name, message=message))



# observer = ObserverBasic("observer_1")
# observable = ObservableBasic("observable_1")
# observable.attach(observer)
# observable.notify("Hello world")