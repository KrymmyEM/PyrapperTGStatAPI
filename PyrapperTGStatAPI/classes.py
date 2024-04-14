from .enums import DatabaseTypes, ResultsType


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


class ChannelStatistic:
    def __init__(self, id, title, username, peer_type, participants_count,
                 avg_post_reach=None, adv_post_reach_12h=None, adv_post_reach_24h=None, adv_post_reach_48h=None,
                 err_percent=None, err24_percent=None, er_percent=None, daily_reach=None, ci_index=None,
                 mentions_count=None, forwards_count=None, mentioning_channels_count=None, posts_count=None,
                 dau=None, wau=None, mau=None, online_count_day_time=None, online_count_night_time=None,
                 messages_count_yesterday=None, messages_count_last_week=None, messages_count_last_month=None,
                 messages_count_total=None):
        self.id = id
        self.title = title
        self.username = username
        self.peer_type = peer_type
        self.participants_count = participants_count
        self.avg_post_reach = avg_post_reach
        self.adv_post_reach_12h = adv_post_reach_12h
        self.adv_post_reach_24h = adv_post_reach_24h
        self.adv_post_reach_48h = adv_post_reach_48h
        self.err_percent = err_percent
        self.err24_percent = err24_percent
        self.er_percent = er_percent
        self.daily_reach = daily_reach
        self.ci_index = ci_index
        self.mentions_count = mentions_count
        self.forwards_count = forwards_count
        self.mentioning_channels_count = mentioning_channels_count
        self.posts_count = posts_count
        self.dau = dau
        self.wau = wau
        self.mau = mau
        self.online_count_day_time = online_count_day_time
        self.online_count_night_time = online_count_night_time
        self.messages_count_yesterday = messages_count_yesterday
        self.messages_count_last_week = messages_count_last_week
        self.messages_count_last_month = messages_count_last_month
        self.messages_count_total = messages_count_total


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
        self.media = None
        if media:
            self.media = Media(**media)


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
        self.mentionId = mentionId
        self.mentionType = mentionType
        self.postId = postId
        self.postLink = postLink
        self.postDate = postDate
        self.channelId = channelId


class Forward:
    def __inint__(self, forwardId, sourcePostId, postId, postLink, postLink, channelId, peerType=None):
        self.forwardId = forwardId
        self.sourcePostId = sourcePostId
        self.postId = postId
        self.postLink = postLink
        self.channelId = channelId
        self.peerType = peerType


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
        self.forwarded_from = None
        if forwarded_from:
            self.forwarded_from = Forward(**forwarded_from)
        self.user_id = user_id
        self.is_deleted = is_deleted
        self.deleted_at = deleted_at
        self.group_id = group_id
        self.text = text
        self.snippet = snippet
        self.media = None
        if media:
            self.media = Media(**media)


class PostStatistic:
    def __init__(self, postId, viewsCount, sharesCount, commentsCount, reactionsCount):
        self.postId = postId
        self.viewsCount = viewsCount
        self.sharesCount = sharesCount
        self.commentsCount = commentsCount
        self.reactionsCount = reactionsCount


class View:
    def __init__(self, date, viewsGrowth):
        self.date = date
        self.viewsGrowth = viewsGrowth


class GroupStatistic:
    def __init__(self, viewsCount, sharesCount, commentsCount, reactionsCount, forwardsCount, mentionsCount, forwards, mentions, views):
        self.viewsCount = viewsCount
        self.sharesCount = sharesCount
        self.commentsCount = commentsCount
        self.reactionsCount = reactionsCount
        self.forwardsCount = forwardsCount
        self.mentionsCount = mentionsCount
        self.forwards = [Forward(**fwd) for fwd in forwards]
        self.mentions = [Mention(**mention) for mention in mentions]
        self.views = [View(**view) for view in views]


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
    def __init__(self, database_type: DatabaseTypes, code, name):
        self.database_type = database_type
        self.code = code
        self.name = name


class MassiveResult:
    def __init__(self, result_type: ResultsType, count = None, total_count = None, channel = None, items = None, channels = None):
        self.result_type = result_type
        if count:
            self.count = count
        if total_count:
            self.total_count = total_count
        if channel:
            self.channel = Channel(**channel)
        
        if items:
            if ResultsType.POST:
                self.items = [Post(**post) for post in items]

            elif ResultsType.STORIES:
                self.items = [Story(**story) for story in items]
            
            elif ResultsType.MENTIONS:
                self.items = [Mention(**mention) for mention in items]

            elif ResultsType.FORWARDS:
                self.items = [Forward(**fr) for fr in items]

        if channels:
            self.channels = [Channel(**chan) for chan in channels]


class DynamicData:
    def __init__(self, dynamic_type, period, **kwargs):
        self.dynamic_type = dynamic_type
        self.period = period

        for key, value in kwargs.items():
            setattr(self, key, value)
