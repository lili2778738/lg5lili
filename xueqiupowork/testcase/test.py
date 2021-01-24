from xueqiupowork.src.app import APP


class Testnowball:
    def test_open(self):
        app=APP()
        app.startapp().Main().gotosearch()
        app.stopapp()