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


