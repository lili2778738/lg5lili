import time
from framework.app import APP


class Test_app:
    def testhandle(self):
        app = APP()
        app.start_app().Main().handle().search()
        app.stop_app()
    def testapp_search(self):
        app=APP()
        app.start_app().Main().goto_search().search()
        time.sleep(10)
        app.stop_app()