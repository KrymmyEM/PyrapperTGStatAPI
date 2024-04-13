
class Channel:
    def __init__(
            self, id, tg_id, link, peer_type, username, active_usernames,
            title, about, image100, image640, participants_count, tgstat_restrictions
        ):
        self.id = id
        self.tg_id = tg_id
        self.link = link
        self.peer_type = peer_type
        self.username = username
        self.active_usernames = active_usernames
        self.title = title
        self.about = about
        self.image100 = image100
        self.image640 = image640
        self.participants_count = participants_count
        self.tgstat_restrictions = tgstat_restrictions


class Media:
    def __init__(self, media_type, **kwargs):
        self.media_type = media_type
        # kwargs содержит дополнительные аргументы, которые могут быть переданы
        for key, value in kwargs.items():
            setattr(self, key, value)


class Story:
    def __init__(
        self, id, date, views, link,
        channel_id, is_expired, expire_at,
        caption, media
        ):
        self.id = id
        self.date = date
        self.views = views
        self.link = link
        self.channel_id = channel_id
        self.is_expired = is_expired
        self.expire_at = expire_at
        self.caption = caption
        self.media = media


class User:
    def __init__(
        self, id, tg_id, username, 
        firstname, lastname
        ):
        self.id = id
        self.tg_id = tg_id
        self.username = username
        self.firstname = firstname
        self.lastname = lastname


class Mention:
    def __init__(self, mentionId, mentionType, postId, postLink, postDate, channelId):
        pass

class Forward:
    def __inint__(self, forwardId, sourcePostId, postId, postLink, postLink, channelId):
        pass


class Post:
    def __init__(
            self, id, date, views, link,
            channel_id, forwarded_from, 
            user_id, is_deleted, deleted_at, 
            group_id, text, snippet, media,
        ):
        self.id = id
        self.date = date
        self.views = views
        self.link = link
        self.channel_id = channel_id
        self.forwarded_from = forwarded_from
        self.user_id = user_id
        self.is_deleted = is_deleted
        self.deleted_at = deleted_at
        self.group_id = group_id
        self.text = text
        self.snippet = snippet
        self.media = media


class CallbackNotify:
    def __init__(
        self, subscription_id,
        subscription_type, event_id,
        event_type, **kwargs
        ):
        self.subscription_id = subscription_id
        self.subscription_type = subscription_type
        self.event_id = event_id
        self.event_type = event_type
        # kwargs содержит дополнительные аргументы, которые могут быть переданы
        for key, value in kwargs.items():
            setattr(self, key, value)


class DatabaseEntity:
    def __init__(self, database_type, code, name):
        self.database_type = database_type
        self.code = code
        self.name = name


class MassiveResult:
    def __init__(self, result_type, count = None, total_count = None, channel = None, items = None, channels = None):
        pass