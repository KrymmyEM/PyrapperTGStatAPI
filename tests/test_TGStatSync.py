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
        categories = tgs.api(enums.RequestsCategory.DATABASE, enums.DatabaseRequests.CATEGORIES)
        countries = tgs.api(enums.RequestsCategory.DATABASE, enums.DatabaseRequests.COUNTRIES)
        languages = tgs.api(enums.RequestsCategory.DATABASE, enums.DatabaseRequests.LANGUAGES)
        self.assertIsInstance(categories, classes.DatabaseEntity, "Database not return DatabaseEntity in categories")
        self.assertIsInstance(countries, classes.DatabaseEntity, "Database not return DatabaseEntity in countries")
        self.assertIsInstance(languages, classes.DatabaseEntity, "Database not return DatabaseEntity in languages")

        self.assertEqual(categories.database_type, enums.DatabaseTypes.CATEGORIES, f"Not correct db type in category : {categories.database_type}")
        self.assertEqual(countries.database_type, enums.DatabaseTypes.COUNTRIES, f"Not correct db type in countries : {countries.database_type}")
        self.assertEqual(languages.database_type, enums.DatabaseTypes.LANGUAGES, f"Not correct db type in languages : {languages.database_type}")

    
    def test_get_channel_info(self):
        tgs = tg_stat.TGStatSync(environ.get("0000"), tests=True)
        data = {
            "status": "ok",
            "response": {
                "id": 321,
                "link": "t.me/varlamov",
                "peer_type": "channel",
                "username": "@varlamov",
                "active_usernames": [
                    "@varlamov"
                ],
                "title": "Varlamov.ru",
                "about": "Илья Варламов. Make Russia warm again! ...",
                "category": "Блоги",
                "country": "Россия",
                "language": "Русский",
                "image100": "//static.tgstat.ru/public/images/channels/_100/ca/caf1a3dfb505ffed0d024130f58c5cfa.jpg",
                "image640": "//static.tgstat.ru/public/images/channels/_0/ca/caf1a3dfb505ffed0d024130f58c5cfa.jpg",
                "participants_count": 154800,
                "tgstat_restrictions": {      # ограничения, наложенные на канал (если ограничений нет - будет возвращен пустой массив)
                    "red_label": True,        # канал помечен красной меткой (за накрутку) на TGStat.ru
                    "black_label": True,      # канал помечен черной меткой (за мошенничество) на TGStat.ru
                }
            }
        }

        result = tgs.get_result(data, enums.ChannelsRequests.GET)
        self.assertIsInstance(dynamic_data, classes.Channel, "Channel result not a Channel type")
    
    
    def test_dynamic_info(self):
        tgs = tg_stat.TGStatSync(environ.get("0000"), tests=True)
        dynamic_data = tgs.get_result("", enums.ChannelsRequests.SUBSCRIBERS)
        self.assertIsInstance(dynamic_data[-1], classes.DynamicData, "Channels SUBSCRIBERS not DynamicData class")
        dynamic_data = tgs.get_result("", enums.ChannelsRequests.SUBSCRIBERS)
        self.assertIsInstance(dynamic_data[-1], classes.DynamicData, "Channels SUBSCRIBERS not DynamicData class")
        dynamic_data = tgs.get_result("", enums.ChannelsRequests.SUBSCRIBERS)
        self.assertIsInstance(dynamic_data[-1], classes.DynamicData, "Channels SUBSCRIBERS not DynamicData class")
        dynamic_data = tgs.get_result("", enums.ChannelsRequests.SUBSCRIBERS)
        self.assertIsInstance(dynamic_data[-1], classes.DynamicData, "Channels SUBSCRIBERS not DynamicData class")
        dynamic_data = tgs.get_result("", enums.ChannelsRequests.SUBSCRIBERS)
        self.assertIsInstance(dynamic_data[-1], classes.DynamicData, "Channels SUBSCRIBERS not DynamicData class")
        dynamic_data = tgs.get_result("", enums.ChannelsRequests.SUBSCRIBERS)
        self.assertIsInstance(dynamic_data[-1], classes.DynamicData, "Channels SUBSCRIBERS not DynamicData class")
        
        
