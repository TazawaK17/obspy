# -*- coding: utf-8 -*-
import os
import io

from obspy.core.event import read_events
from obspy.io.nied.fnetmt import _is_fnetmt_catalog


class TestFNETMTCatalogReading():
    """
    Test everything related to reading an F-net moment tensor catalog.
    """
    @classmethod
    def setup_class(cls):
        # Directory where the test files are located
        cls.path = os.path.dirname(__file__)

    def test_read_fnetmt_catalog(self):
        testfile = os.path.join(self.path, 'data', 'FNETMTCATALOG')
        cat = read_events(testfile, 'FNETMT')
        assert len(cat) == 1
        ev = cat[0]
        assert len(ev.origins) == 2
        assert len(ev.magnitudes) == 2

    def test_read_fnetmt_catalog_from_open_files(self):
        """
        Tests that reading an F-net moment tensor file from an open file works.
        """
        testfile = os.path.join(self.path, 'data', 'FNETMTCATALOG')
        with open(testfile, "rb") as fh:
            read_events(fh)

    def test_read_fnetmt_catalog_from_bytes_io(self):
        """
        Tests that reading an F-net moment tensor file from a BytesIO objects
        works.
        """
        testfile = os.path.join(self.path, 'data', 'FNETMTCATALOG')
        with open(testfile, "rb") as fh:
            buf = io.BytesIO(fh.read())

        with buf:
            read_events(buf)

    def test_is_fnetmt_catalog(self):
        """
        This tests the _is_fnetmt_catalog method by validating that each file
        in the data directory is an F-net catalog file and each file in the
        working directory is not.

        The filenames are hard coded so the test will not fail with future
        changes in the structure of the package.
        """
        # F-net catalog file names.
        fnetmt_filenames = ['FNETMTCATALOG']

        # Non F-net file names.
        non_fnetmt_filenames = ['test_fnetmt_reading.py',
                                '__init__.py']
        # Loop over F-net files
        for _i in fnetmt_filenames:
            filename = os.path.join(self.path, 'data', _i)
            is_fnetmt = _is_fnetmt_catalog(filename)
            assert is_fnetmt
        # Loop over non F-net files
        for _i in non_fnetmt_filenames:
            filename = os.path.join(self.path, _i)
            is_fnetmt = _is_fnetmt_catalog(filename)
            assert not is_fnetmt
