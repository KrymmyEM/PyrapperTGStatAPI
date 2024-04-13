import unittest
from PyrapperTGStatAPI import classes, enums, exceptions, tg_stat


class TGStatSyncTest(unittest.TestCase):

    def test_token_exeptions(self):
        self.assertRaises(exceptions.TGStatAuthError, tg_stat.TGStatSync(""))
        self.assertRaises(exceptions.TGStatAuthError, tg_stat.TGStatSync("000"))
