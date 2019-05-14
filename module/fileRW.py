#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QFileDialog
import os

class fileClass():

    def read_file(self):
        fileName_choose, filetype = QFileDialog.getOpenFileNames(None,
                                                                 '多选文件',
                                                                 '',
                                                                 'All Files (*);;Excel 文件 (*.xlsx)')
        return fileName_choose

    def write_file(self):
        fileName_choose, filetype = QFileDialog.getSaveFileName(None,  
                                                                "文件保存",  
                                                                '', # 起始路径 
                                                                "All Files (*);;Excel 文件 (*.xlsx)")
        return fileName_choose

    def read_one_file(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(None,
                                                                 '单选文件',
                                                                 '',
                                                                 'All Files (*);;Excel 文件 (*.xlsx)')
        return fileName_choose