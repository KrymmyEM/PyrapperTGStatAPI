from requests import Request, Session
from aiohttp import ClientSession

from .enums import *
from .classes import *
from .exceptions import * 


class TGStatSync():

    base_url = "https://api.tgstat.ru"
    
    def __init__(self, token):
        self.token = token
        self.session = Session()

        
    def _send_request(self, method, url, data, **kwargs):
        pass
    
    
    def _build_result(self, data, category):
        pass


    def api(self, category, sub_category, **kwargs):
        pass