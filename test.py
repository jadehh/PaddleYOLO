#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : test.py
# @Author   : jade
# @Date     : 2023/4/17 14:40
# @Email    : jadehh@1ive.com
# @Software : Samples
# @Desc     :
from dataset_tools import CreateYearsDatasets
def CreateDatasets():
    CreateYearsDatasets("F:\数据集\VOC数据集\危险品标志检测数据集")
if __name__ == '__main__':
    CreateDatasets()