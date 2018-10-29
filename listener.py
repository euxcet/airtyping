from leap import Leap
from handler import Handler

class Listener(Leap.Listener):
    def on_connect(self, controller):
        print "Connected"
        self.handler = Handler()

    def on_disconnect(self, controller):
        print "Disconnected"

    def on_frame(self, controller):
        self.handler.handle(controller)
