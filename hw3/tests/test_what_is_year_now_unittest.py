import json
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

from hw3.what_is_year_now import what_is_year_now

YMD_RESPONSE = {"currentDateTime": "2020-04-19T11:46Z"}
DMY_RESPONSE = {"currentDateTime": "19.04.2019T11:46Z"}
INVALID_RESPONSE = {"currentDateTime": "19_04_2020T11:46Z"}


class TestWhatIsYearNow(unittest.TestCase):
    @patch("urllib.request.urlopen")
    def test_ymd(self, mock_urlopen):
        mm = MagicMock()
        mm.read.return_value = json.dumps(YMD_RESPONSE)
        mm.__enter__.return_value = mm
        mock_urlopen.return_value = mm

        self.assertEqual(what_is_year_now(), 2020)

    @patch("urllib.request.urlopen")
    def test_dmy(self, mock_urlopen):
        mm = MagicMock()
        mm.read.return_value = json.dumps(DMY_RESPONSE)
        mm.__enter__.return_value = mm
        mock_urlopen.return_value = mm

        self.assertEqual(what_is_year_now(), 2019)

    @patch("urllib.request.urlopen")
    def test_invalid_format(self, mock_urlopen):
        mm = MagicMock()
        mm.read.return_value = json.dumps(INVALID_RESPONSE)
        mm.__enter__.return_value = mm
        mock_urlopen.return_value = mm

        with self.assertRaises(ValueError):
            what_is_year_now()
