import jsonpath
import requests


class AppraiseManageApi:

    def __init__(self):
        url = "https://performance.beta-test.rishiqing.com/task/j_spring_security_check"
        data = {"j_username": "13811111111", "j_password": "123456", "remember-me": "true"}
        r = requests.post(url, data=data)
        self.token = jsonpath.jsonpath(r.json(), "$..token")[0]
        # print(self.token)
        self.headers = {"token": self.token}

    # 考核管理 考核列表
    def all(self):
        url = "https://performance.beta-test.rishiqing.com/task/performance/appraisals/all"
        r = requests.get(url, headers=self.headers)
        return r.json()


    # 考核 新建
    def appraise(self):
        pass

    # 批量发起考核
    def batch(self):
        pass

    # 批量发起考核校验
    def batchHas(self):
        pass

    # 考核详情
    def details(self):
        pass

    # 考核 更新-个人
    def personup(self):
        pass

    # 考核 删除-个人
    def persondelete(self):
        pass

    # 考核内容 流程详情
    def flowInfo(self):
        pass

    # 考核内容 评论列表
    def comments(self):
        pass

    # 考核内容 操作记录列表
    def operationList(self):
        pass

    # 考核内容 重置流程
    def reset(self):
        pass

    # 考核流程 撤销流程
    def recall(self):
        pass

    # 考核流程 跳过任务
    def skip(self):
        pass

    # 考核流程 转交任务
    def transfer(self):
        pass

    # 考核 开始评分
    def startScore(self):
        pass

    # 考核 考核内容确认通过并提交
    def confirmSubmit(self):
        pass

    # 考核 批量评分
    def startScoreBatch(self):
        pass

    # 考核 考核结果确认通过并提交
    def resultConfirmSubmit(self):
        pass

    # 考核 调整结果
    def changeResult(self):
        pass

    # 考核 获取某个周期下哪些用户已经有对应的考核
    def has(self):
        pass

    # 考核 获取用户最后一次选择的考核周期副本
    def lastPeriod(self):
        pass

    # 考核 考核管理导出
    def export(self):
        pass

    # 考核 历史周期列表
    def periodHistories(self):
        pass

    # 获取当前可见的评分总结
    def reviewsget(self):
        pass

    # 发表一个评分总结
    def reviewsput(self):
        pass

    # 邀请同事提交确认
    def submitInvite(self):
        pass

    # 考核管理等级分布
    def statistics(self):
        pass

    # 获取考核所属的评分规则
    def rule(self):
        pass
