from appium.webdriver.common.mobileby import MobileBy


def b(fun):
    def run(*args,**kwargs):
        instance=args[0]
        black_list = [(MobileBy.ID, "com.xueqiu.android:id/iv_close")]
        try:
            return fun(*args,**kwargs)
        except:
            for black in black_list:
                ele = instance.basedriver.find_elements(*black)
                if len(ele) > 0:
                    ele[0].click()
                    break
            return fun(*args,**kwargs)
    return run