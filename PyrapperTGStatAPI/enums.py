from enum import Enum


class RequestsMethods(Enum):
    GET = 1
    POST = 2


class RequestsCategory(Enum):
    CHANNELS = "channels"
    POSTS = "posts"
    STORIES = "stories"
    WORDS = "words"
    CALLBACK = "callback"
    USAGE = "usage"
    DATABASE = "database"


class ChannelsRequests(Enum):
    GET = ("get", RequestsMethods.GET)
    SEARCH = ("search", RequestsMethods.GET)
    STAT = ("stat", RequestsMethods.GET)
    POSTS = ("posts", RequestsMethods.GET)
    STORIES = ("stories", RequestsMethods.GET)
    MENTIONS = ("mentions", RequestsMethods.GET)
    FORWARDS = ("forwards", RequestsMethods.GET)
    SUBSCRIBERS = ("subscribers", RequestsMethods.GET)
    VIEWS = ("views", RequestsMethods.GET)
    AVG_POSTS_REACH = ("avg-posts-reach", RequestsMethods.GET)
    ER = ("er", RequestsMethods.GET)
    ERR = ("err", RequestsMethods.GET)
    ERR24 = ("err24", RequestsMethods.GET)
    ADD = ("add", RequestsMethods.POST)


class PostsRequests(Enum):
    GET = ("get", RequestsMethods.GET)
    STAT = ("stat", RequestsMethods.GET)
    STAT_MULTI = ("stat-multi", RequestsMethods.GET)
    SEARCH = ("search", RequestsMethods.GET)


class StoriesRequests(Enum):
    GET = ("get", RequestsMethods.GET)
    STAT = ("stat", RequestsMethods.GET)
    STAT_MULTI = ("stat-multi", RequestsMethods.GET)


class WordsRequests(Enum):
    MENTIONS_BY_PERIOD = ("mentions-by-period", RequestsMethods.GET)
    MENTIONS_BY_CHANNELS = ("mentions-by-channels", RequestsMethods.GET)