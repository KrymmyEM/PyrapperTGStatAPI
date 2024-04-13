from requests import Request, Session
import aiohttp

from .enums import *
from .classes import *
from .exceptions import * 


class TGStatSync(Session):
    
    def __init__(self, token):
        super().__init__()
        self.token = token
        