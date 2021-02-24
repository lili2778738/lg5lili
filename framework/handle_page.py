from appium.webdriver.common.mobileby import MobileBy

def HandlePage(fun):
    def run(*args,**kwargs):
        black_list=[(MobileBy.ID,"com.xueqiu.android:id/iv_close")]
        try:
           fun(*args,**kwargs)
           return fun
        except Exception as e:
            for black in black_list:
                ele=args[0].basedriver.find_elements(black)
                if len(ele)>0:
                    result1ist=args[0].basedriver.find_element(*black)
                    result1ist[0].click()
                    fun(*args,**kwargs)
                    return fun
            raise e
        return run