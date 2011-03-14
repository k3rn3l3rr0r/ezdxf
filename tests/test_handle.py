#!/usr/bin/env python
#coding:utf-8
# Author:  mozman -- <mozman@gmx.at>
# Purpose: test handle
# Created: 12.03.2011
# Copyright (C) 2011, Manfred Moitzi
# License: GPLv3

import sys
import unittest

from ezdxf.handle import HandleGenerator

class TestHandleGenerator(unittest.TestCase):
    def test_next(self):
        handles = HandleGenerator('100')
        self.assertEqual('101', handles.next)

    def test_seed(self):
        handles = HandleGenerator('200')
        handles.next
        self.assertEqual('201', handles.seed)

    def test_reset(self):
        handles = HandleGenerator('200')
        handles.reset('300')
        self.assertEqual('300', handles.seed)

if __name__=='__main__':
    unittest.main()