from typing import Optional
import json
from requests import Request, Session
from aiohttp import ClientSession

from .enums import *
from .classes import *
from .exceptions import * 


class TGStatSync:

    base_url = "https://api.tgstat.ru"
    
    def __init__(self, token, **kwargs):
        self.token = token
        self.session = Session()
        if not kwargs.get("tests", False):
            result = self.session.get(self.base_url + "/usage/stat", param={"token":token}).json()
            if data['status'] == "error":
                raise TGStatAuthError(data["error"])
            
        
    def _send_request(self, method: RequestsMethods, url: str, **kwargs):
        kwargs["token"] = self.token
        response = self.session.request(method=method.value, url=url, params=kwargs)
        return response.json()
    
    
    def _check_catgory(self, category, sub_category):
        if not isinstance(category, RequestsCategory):
            raise TGStatTypeError(type(category), type(RequestsCategory), category._name_)
        
        if not type(sub_category) in [ChannelsRequests, PostsRequests, StoriesRequests, WordsRequests,
                                        CallbackRequests, UsageRequests, DatabaseRequests]:
            raise TGStatTypeError(type(category), [ChannelsRequests, PostsRequests, StoriesRequests, WordsRequests,
                                        CallbackRequests, UsageRequests, DatabaseRequests], sub_category._name_)
        
        return True

    
    def _build_result(self, data, sub_category: Optional[
                    ChannelsRequests, PostsRequests, StoriesRequests, WordsRequests,
                    CallbackRequests, UsageRequests, DatabaseRequests
                ]):
        self._check_catgory(category, sub_category)

        if isinstance(data, str):
            try:
                data = json.loads(data)
            except:
                raise TGStatException("Incorrect data value")

        if data['status'] == "error":
            raise TGStatAPIError(data["error"])
        
        class_parser = None
        kwargs = {}
        if sub_category in [ChannelsRequests.SEARCH, ChannelsRequests.POSTS, ChannelsRequests.STORIES,
                            ChannelsRequests.MENTIONS, ChannelsRequests.FORWARDS, PostsRequests.SEARCH,
                            PostsRequests.STAT]:
            class_parser = MassiveResult
            
            key = "result_type"

            if sub_category in [ChannelsRequests.SEARCH]:
                kwargs[key] = ResultsType.CHANNELS

            elif sub_category in [ChannelsRequests.POSTS, PostsRequests.SEARCH]:
                kwargs[key] = ResultsType.POST

            elif sub_category in [ChannelsRequests.STORIES]:
                kwargs[key] = ResultsType.STORIES

            elif sub_category in [ChannelsRequests.FORWARDS]:
                kwargs[key] = ResultsType.FORWARDS
            
            elif sub_category in [ChannelsRequests.MENTIONS, WordsRequests.MENTIONS_BY_CHANNELS]:
                kwargs[key] = ResultsType.MENTIONS
                
            else:
                raise TGStatException("Unsupported Enum")
        
        return data["response"]


    def get_result(self, data, sub_category: Optional[
                    ChannelsRequests, PostsRequests, StoriesRequests, WordsRequests,
                    CallbackRequests, UsageRequests, DatabaseRequests
                ]):
                
        self._check_catgory(category, sub_category)

        return self._build_result(data, category, sub_category)


    def api(self, category: RequestsCategory, 
            sub_category: Optional[
                    ChannelsRequests, PostsRequests, StoriesRequests, WordsRequests,
                    CallbackRequests, UsageRequests, DatabaseRequests
                ], 
            **kwargs):

        self._check_catgory(category, sub_category)

        first_postfix = category.value
        last_postfix, method = sub_category.value
        sending_url = self.base_url + "/" + first_postfix + "/" + last_postfix
        response = self._send_request(method, sending_url, **kwargs)
        result = self._build_result(response, category)

        return result


