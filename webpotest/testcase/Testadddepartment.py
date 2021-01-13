from selenium.webdriver.common.by import By

from webpotest.Sourcecode.Main import main

class Test_add:
    def setup(self):
        self.m=main()
    def teardown(self):
        #清除添加的部门信息
        self.m.go_to_addressbook().dele_section()
        self.m._driver.quit()
    # 成功添加部门
    def testadd(self):
        result=self.m.go_to_addressbook().go_to_section().section('测试部').get_list_section()
        assert  '测试部' in result
    # 添加部门失败
    def testadd_fail(self):
        self.m.go_to_addressbook().go_to_section().section('测试部')
        self.m.go_to_addressbook().go_to_section().section('测试部')
        infromation=self.m.find(By.ID,'js_tips').text
        assert infromation=='该部门已存在'
    #添加部门名称为空
    def testadd_null(self):
        webmessage=self.m.go_to_addressbook().go_to_section().section_null()
        assert webmessage=="请输入部门名称"