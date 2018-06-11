import logging
import os
import time

# 文件保存路径
log_path = 'D:\HAIZOL\\result\logs'


class Log:
    def __init__(self):
        # 文件命名
        self.logname = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        # 日志输出格式
        self.formatter = logging.Formatter(
            '%(levelname)s - %(asctime)s - %(name)s - %(message)s')

    def _console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        # 创建一个StreamHandler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 避免日志重复
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        fh.close()

    def debug(self, message):
        self._console('debug', message)

    def info(self, message):
        self._console('info', message)

    def error(self, message):
        self._console('error', message)

    def warning(self, message):
        self._console('warning', message)


if __name__ == '__main__':
    log = Log()
    log.info('test start')
    log.warning('test end')

