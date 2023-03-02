import logging
import os
def logger_config(log_path='../Mylog/', log_filename="mylog.log", logging_name='mylog'):
    os.makedirs(log_path, mode=0o755, exist_ok=True)
    # 获取logger对象
    logger = logging.getLogger(logging_name)
    logger.setLevel(logging.INFO)
    # 创建一个handler,用于写入日志文件
    fh = logging.FileHandler(log_filename, mode='a+')
    fh.setFormatter(logging.Formatter("[%(asctime)s]:%(levelname)s:%(message)s"))
    logger.addHandler(fh)
    # 创建一个handler，输出到控制台
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(ch)
    return logger