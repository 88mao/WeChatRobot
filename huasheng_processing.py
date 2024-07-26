import re


class huasheng_processing():

    def __init__(self, msg):
        self.msg = msg

    def processingAtMsg(self):
        '''
        处理被@的消息
        '''
        q = re.sub(r"@.*?[\u2005|\s]", "", self.msg).replace(" ", "")
        print("华盛处理消息：" + q)
        # 判断查询财务账单汇总
        if q == '财务账单汇总':
            return self.processingFinancialStatementSummary(q)
        return "请选择正确的指令"

    def processingFinancialStatementSummary(self, content):
        '''
        处理财务账单汇总
        '''
        print("处理财务：" + content)
        return "处理财务账单汇总"
