import threading


class Adapter(threading.Thread):
    def __init__(self, adapter):
        threading.Thread.__init__(self)
        self.adapter = adapter()

    def run(self):
        while True:
            self.adapter.run()
