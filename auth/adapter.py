from threading import Thread


class Adapter(Thread):
    def __init__(self, auth):
        super().__init__()
        self.auth = auth()
        self.setDaemon(True)

    def run(self):
        while True:
            self.auth.run()
