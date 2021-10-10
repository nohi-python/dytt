

class ServiceException(Exception):  # 继承异常类
    def __init__(self, name, reason):
        self.name = name
        self.reason = reason
