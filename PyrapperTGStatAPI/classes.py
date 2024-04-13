
class Channel:
    def __init__(
            self, id, tg_id, link, peer_type, username, active_usernames,
            title, about, image100, image640, participants_count, tgstat_restrictions
        ):
        pass


class Media:
    def __init__(self, media_type, **kwargs):
        pass


class Story:
    def __init__(
        self, id, date, views, link,
        channel_id, is_expired, expire_at,
        caption, media
    ):
        pass


class User:
    def __init__(
        self, id, tg_id, username, 
        firstname, lastname
    ):
        pass


class Post:
    def __init__(
        self, id, date, views, link,
        channel_id, forwarded_from, 
        user_id, is_deleted, deleted_at, 
        group_id, text, snippet, media,
    ):
        pass


class CallbackNotify:
    def __init__(
        self, subscription_id,
        subscription_type, event_id,
        event_type, **kwargs
    ):
        passs