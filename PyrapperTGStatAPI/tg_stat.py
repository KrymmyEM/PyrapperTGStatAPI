from requests import Request, Session
from aiohttp import ClientSession

from .enums import *
from .classes import *
from .exceptions import * 


class TGStatSync(Session):
    
    def __init__(self, token):
        super().__init__()
        self.token = token
