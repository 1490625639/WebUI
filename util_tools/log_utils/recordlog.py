# -*- coding: UTF-8 -*-
"""
Project ：WebUI 
File    ：recordlog.py
Author  ：张以白
Date    ：2024/6/19 22:36 
Desc    : 封装日志文件
"""
import colorlog
import logging
import os.path
import time
from logging.handlers import RotatingFileHandler #按文件大小滚动备份
from config import setting

log_path = setting.FILE_PATH['log']

if not os.path.exists(log_path):
    os.mkdir(log_path)

logfile_name = log_path + r'\test{}.log'.format(time.strftime('%Y%m%d'))


class RecordLog:
    def __init__(self):
        pass
    @classmethod
    def lgo_color(cls):
        log_color_config={
            'DEBUG':'cyan',
            'INFO':'green',
            'WARNING':'yellow',
            'ERROE':'red',
            'CRITICAL':'red'
        }
        formater=colorlog.ColoredFormatter(
            '%(log_color)s %(levelname)s-%(asctime)s-%(filename)s:%(lineno)d-[%(module)s:%(funcName)s]-%(message)s',log_colors=log_color_config)
        return formater
    def output_logging(self):
        logger = logging.getLogger(__name__)
        stream_format=self.lgo_color()
        if not logger.handlers:
            logger.setLevel(logging.DEBUG)
            log_format=logging.Formatter(
                '%(levelname)s-%(asctime)s-%(filename)s:%(lineno)d-[%(module)s:%(funcName)s]-%(message)s'
            )
            # 日志文件输出到控制台
            sh=logging.StreamHandler()
            sh.setLevel(logging.DEBUG)
            sh.setFormatter(stream_format)
            logger.addHandler(sh)

            # 日志信息输出到指定文件中
            fh=RotatingFileHandler(filename=logfile_name,mode='a',maxBytes=5242880,backupCount=7,encoding='utf-8')
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(stream_format)
            logger.addHandler(fh)
        return logger
reco=RecordLog()
logs=reco.output_logging()
#
# logs.info("这是info信息")
# logs.error("这是error信息")
# logs.debug("debug")
# logs.critical("crioaowijfo")
# logs.debug("debug信息")
# logs.warning("warning信息")