from os import environ
import unittest

from dotenv import load_dotenv
from PyrapperTGStatAPI import classes, enums, exceptions, tg_stat

load_dotenv()

class TGStatSyncTest(unittest.TestCase):

    def test_token_exeptions(self):
        self.assertRaises(exceptions.TGStatAuthError, tg_stat.TGStatSync(""))
        self.assertRaises(exceptions.TGStatAuthError, tg_stat.TGStatSync("000"))

        
    def test_get_databases(self):
        tgs = tg_stat.TGStatSync(environ.get("TOKEN"))
        self.assertIsInstance(tgs.api(enums.RequestsCategory.DATABASE, enums.DatabaseRequests.CATEGORIES), classes.DatabaseEntity, "Database not return DatabaseEntity in categories")
        self.assertIsInstance(tgs.api(enums.RequestsCategory.DATABASE, enums.DatabaseRequests.COUNTRIES), classes.DatabaseEntity, "Database not return DatabaseEntity in countries")
        self.assertIsInstance(tgs.api(enums.RequestsCategory.DATABASE, enums.DatabaseRequests.LANGUAGES), classes.DatabaseEntity, "Database not return DatabaseEntity in langiages")
    
    def test_get_channel_info(self):
        tgs = tg_stat.TGStatSync(environ.get("TOKEN"))
        self.assertIsInstance(tgs.api(enums.RequestsCategory.CHANNELS, enums.ChannelsRequests.GET, channelId="https://t.me/aiogram_pcr"), classes.Channel)
        
