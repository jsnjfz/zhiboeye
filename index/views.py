# coding: utf-8
from django.shortcuts import render
from django.views.generic.base import View

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import PlatForm, ChannelDict, PlatFormDict


# Create your views here.


class IndexView(View):
    def get(self, request):
        all_info = PlatForm.objects.all().order_by('-watch_num')
        filter_info = PlatForm.objects.all().order_by('-watch_num')[:200]
        all_num = all_info.count()

        all_channel = ChannelDict.objects.all().order_by('channel_type')

        all_platform = PlatFormDict.objects.filter(status=1)

        # 取出筛选频道
        type_name = request.GET.get('name', "")
        if type_name:
            filter_info = all_info.filter(channel_name=type_name)[:200]

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation
        p = Paginator(filter_info, 18, request=request)

        info = p.page(page)

        return render(request, "index.html", {
            "info": info,
            "all_channel": all_channel,
            "all_platform": all_platform,
            "all_num": all_num,
            "type_name": type_name,
        })
