from typing import Optional
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

        
    def _send_request(self, method: RequestsMethods, url: str, data, **kwargs):
        pass
    
    
    def _build_result(self, data, category):
        pass


    def api(self, category: RequestsCategory, 
            sub_category: Optional[
                    ChannelsRequests, PostsRequests, StoriesRequests, WordsRequests,
                    CallbackRequests, UsageRequests, DatabaseRequests
                ], 
            **kwargs):

        if not isinstance(category, RequestsCategory):
            raise TGStatTypeError(type(category), type(RequestsCategory), category._name_)
        
        if not type(sub_category) in [ChannelsRequests, PostsRequests, StoriesRequests, WordsRequests,
                                        CallbackRequests, UsageRequests, DatabaseRequests]:
            raise TGStatTypeError(type(category), [ChannelsRequests, PostsRequests, StoriesRequests, WordsRequests,
                                        CallbackRequests, UsageRequests, DatabaseRequests], sub_category._name_)

        first_postfix = category.value
        last_postfix, method = sub_category.value
