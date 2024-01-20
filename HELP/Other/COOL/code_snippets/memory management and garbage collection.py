class MysteriosClass:
    _instances = []

    def __init__(self):
        self._instances.append(self)

    def __del__(self):
        print("Destructor called for", self)

def create_objects():
    for _ in range(3):
        MysteriosClass()

create_objects()
import gc
gc.collect()