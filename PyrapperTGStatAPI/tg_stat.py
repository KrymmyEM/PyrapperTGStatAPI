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

            data = {
                ChannelsRequests.SEARCH: ResultsType.CHANNELS,
                ChannelsRequests.POSTS: ResultsType.POST, 
                PostsRequests.SEARCH: ResultsType.POST,
                ChannelsRequests.STORIES: ResultsType.STORIES,
                ChannelsRequests.FORWARDS: ResultsType.FORWARDS,
                ChannelsRequests.MENTIONS:ResultsType.MENTIONS, 
                WordsRequests.MENTIONS_BY_CHANNELS:ResultsType.MENTIONS
            }

            try:
                kwargs[key] = data[sub_category]
            except:
                raise TGStatException("Unsupported Enum")
            
            kwargs.update(data["response"])
        
        elif sub_category in [
                                ChannelsRequests.SUBSCRIBERS, ChannelsRequests.VIEWS, ChannelsRequests.AVG_POSTS_REACH,
                                ChannelsRequests.ER, ChannelsRequests.ERR, ChannelsRequests.ERR24,
                                WordsRequests.MENTIONS_BY_PERIOD
                            ]:
            pass
        
        return class_parser(**kwargs)


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


