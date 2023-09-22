import jsonpath
import requests

from utils.schema_utils import SchemaUitls


class TestMyPerformance:


    def setup_class(self):
        url = "https://performance.beta-test.rishiqing.com/task/j_spring_security_check"
        data = {"j_username":"13811111111", "j_password":"123456","remember-me":"true"}
        r = requests.post(url, data=data)
        self.token = jsonpath.jsonpath(r.json(), "$..token")[0]
        # print(self.token)
        self.headers = {"token":self.token}


    # 获取我的邀请同事列表
    def test_get_invitingColleagues(self):
        pass

    # 我的绩效-各种维度单独算,用cycle传参，all,monthly,quarter,annual,semiAnnual,custom
    def test_my(self):
        r = requests.get("https://performance.beta-test.rishiqing.com/task/performance/appraisals/my?type=all&max=20&offset=0",
                         headers=self.headers)
        print(r.json())
        assert r.json()['msg'] == 'ok'
        # print(r.status_code)
        # print(SchemaUitls.schema_validate_by_file(r.json(), 'schema_performance_my.json'))

    # 考核内容确认列表
    def test_contentConfirm(self):
        pass

    # 结果值录入列表
    def test_resultValue(self):
        pass

    # 评分列表
    def test_scoreList(self):
        pass

    # 考核结果确认列表
    def test_resultConfirm(self):
        pass

    # 考核结果校准列表
    def test_resultConfirm_calibrationList(self):
        pass

    # 考核结果校准
    def test_resultConfirm_calibration(self):
        pass

    # 周期列表
    def test_periodList(self):
        pass

    # 我的待办提示
    def test_tip(self):
        pass

    # 考核对象列表
    def test_objectList(self):
        pass

    # 录入结果值
    def test_entry(self):
        pass

    # 指标评分
    def test_score(self):
        pass

    # 直接评定总分
    def test_totalScore(self):
        pass

    # 结果值批量录入 下载模版
    def test_entryDownload(self):
        pass

    # 结果值批量录入 上传模版
    def test_entryUpload(self):
        pass

    # 我的绩效-根据考核周期和考核对象获取考核id
    def test_getId(self):
        pass
