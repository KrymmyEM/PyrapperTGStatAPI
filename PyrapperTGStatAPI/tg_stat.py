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
        result = self.session.get(self.base_url + "/usage/stat", param={"token":token}).json()
        if data['status'] == "error":
            raise TGStatAuthError(data["error"])
            
        
    def _send_request(self, method: RequestsMethods, url: str, **kwargs):
        kwargs["token"] = self.token
        response = self.session.request(method=method.value, url=url, params=kwargs)
        return response.json()
    
    
    def _build_result(self, data, category):
        if data['status'] == "error":
            raise TGStatAPIError(data["error"])
        
        return data["response"]


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
        sending_url = self.base_url + "/" + first_postfix + "/" + last_postfix
        response = self._send_request(method, sending_url, **kwargs)
        result = self._build_result(response, category)

        return result


