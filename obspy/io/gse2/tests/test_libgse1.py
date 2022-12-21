#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
The libgse1 test suite.
"""
import os

from obspy.io.gse2 import libgse1
from obspy.io.gse2.libgse2 import ChksumError
import pytest


class TestLibGSE1():
    """
    Test cases for libgse1.
    """
    @classmethod
    def setup_class(cls):
        # directory where the test files are located
        cls.path = os.path.join(os.path.dirname(__file__), 'data')

    def test_verify_checksums(self):
        """
        Tests verifying checksums for CM6 encoded GSE1 files.
        """
        # 1
        fh = open(os.path.join(self.path, 'acc.gse'), 'rb')
        libgse1.read(fh, verify_chksum=True)
        fh.close()
        # 2
        fh = open(os.path.join(self.path, 'y2000.gse'), 'rb')
        libgse1.read(fh, verify_chksum=True)
        fh.close()
        # 3
        fh = open(os.path.join(self.path, 'loc_STAU20031119011659.z'), 'rb')
        libgse1.read(fh, verify_chksum=True)
        fh.close()
        # 4 - second checksum is wrong
        fh = open(os.path.join(self.path, 'GRF_031102_0225.GSE.wrong_chksum'),
                  'rb')
        libgse1.read(fh, verify_chksum=True)  # correct
        with pytest.raises(ChksumError):
            libgse1.read(fh, verify_chksum=True)
        fh.close()
