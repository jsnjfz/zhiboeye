# coding:utf-8
__author__ = 'fz'
__date__ = '2017/3/5 10:51'

from django.db import models
from datetime import datetime


# Create your models here.
class PlatForm(models.Model):
    platform_name = models.CharField(max_length=100, verbose_name=u"平台名称")
    platform_type = models.CharField(max_length=20, verbose_name=u"平台类型")
    # platform_desc = models.CharField(max_length=100, verbose_name=u"平台描述")
    channel_name = models.CharField(max_length=100, verbose_name=u"频道名称")
    channel_type = models.CharField(max_length=100, verbose_name=u"频道类型")
    # channel_desc = models.CharField(max_length=100, verbose_name=u"频道描述")
    room_id = models.IntegerField(verbose_name=u"房间号")
    room_desc = models.CharField(max_length=100, verbose_name=u"房间描述")
    room_thumb = models.CharField(max_length=100, verbose_name=u"房间图片快照")
    room_status = models.IntegerField(choices=((1, u"在线"), (2, u"离线")), verbose_name=u"房间状态")
    name = models.CharField(max_length=100, verbose_name=u"主播名称")
    watch_num = models.BigIntegerField(verbose_name=u"观看人数")
    follow_num = models.BigIntegerField(verbose_name=u"关注人数")
    url = models.URLField(max_length=100, verbose_name=u"房间链接")
    time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    # status = models.IntegerField(choices=((0, u"无效"), (1, u"有效")),default = 1, verbose_name=u"状态")

    class Meta:
        verbose_name = u"直播平台信息"
        verbose_name_plural = verbose_name

    # def __unicode__(self):
    #     return '{0}({1})'.format(self.code, self.email)


class PlatFormDict(models.Model):
    platform_type = models.CharField(max_length=100, verbose_name=u"平台类型")
    platform_name = models.CharField(max_length=100, verbose_name=u"平台名称")
    status = models.IntegerField(choices=((0, u"无效"), (1, u"有效")), default=1, verbose_name=u"状态")


class ChannelDict(models.Model):
    channel_type = models.CharField(max_length=100, verbose_name=u"频道类型")
    channel_name = models.CharField(max_length=100, verbose_name=u"频道名称")