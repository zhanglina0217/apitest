from api.appraisemanage_api import AppraiseManageApi


class TestAppraiseManageApi:

    def setup_class(self):
        self.appraisemanage_api = AppraiseManageApi()


    # 考核管理 考核列表
    def test_all(self):
        # print(self.appraisemanage_api.all())
        assert self.appraisemanage_api.all()['code'] == 200
        assert self.appraisemanage_api.all()['msg'] == 'ok'


    def test_appraise(self):
        assert False

    def test_batch(self):
        assert False

    def test_batch_has(self):
        assert False

    def test_details(self):
        assert False

    def test_personup(self):
        assert False

    def test_persondelete(self):
        assert False

    def test_flow_info(self):
        assert False

    def test_comments(self):
        assert False

    def test_operation_list(self):
        assert False

    def test_reset(self):
        assert False

    def test_recall(self):
        assert False

    def test_skip(self):
        assert False

    def test_transfer(self):
        assert False

    def test_start_score(self):
        assert False

    def test_confirm_submit(self):
        assert False

    def test_start_score_batch(self):
        assert False

    def test_result_confirm_submit(self):
        assert False

    def test_change_result(self):
        assert False

    def test_has(self):
        assert False

    def test_last_period(self):
        assert False

    def test_export(self):
        assert False

    def test_period_histories(self):
        assert False

    def test_reviewsget(self):
        assert False

    def test_reviewsput(self):
        assert False

    def test_submit_invite(self):
        assert False

    def test_statistics(self):
        assert False

    def test_rule(self):
        assert False
