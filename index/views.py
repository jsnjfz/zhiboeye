# coding: utf-8
import json

from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q
# from pure_pagination import Paginator, PageNotAnInteger

from .models import PlatForm, ChannelDict, PlatFormDict


# Create your views here.


class IndexView(View):
    def get(self, request):
        # all_info = PlatForm.objects.all().order_by('-watch_num')
        # filter_info = PlatForm.objects.all().order_by('-watch_num')[:200]
        # all_num = all_info.count()

        all_channel = ChannelDict.objects.all().order_by('id')

        all_platform = PlatFormDict.objects.filter(status=1)

        # 取出筛选频道
        type_name = request.GET.get('name', "")
        # if type_name:
        #     filter_info = all_info.filter(channel_name=type_name)[:200]

        # try:
        #     page = request.GET.get('page', 1)
        # except PageNotAnInteger:
        #     page = 1
        #
        # # Provide Paginator with the request object for complete querystring generation
        # p = Paginator(filter_info, 18, request=request)
        #
        # info = p.page(page)

        return render(request, "index.html", {
            # "info": info,
            "all_channel": all_channel,
            "all_platform": all_platform,
            # "all_num": all_num,
            "type_name": type_name, }
        )



def ajaxchannel(request):
    # 取出筛选频道
    search = request.POST.get('search', "")
    plat_name = request.POST.get('site', "all")
    type_name = request.POST.get('classify', "")
    filter_info = PlatForm.objects.all().order_by('-watch_num')[:60].values('url', 'name', 'room_thumb', 'watch_num',
                                                                      'room_desc', 'platform_name')
    if search:
        filter_info = PlatForm.objects.filter(Q(room_desc__contains=search) | Q(name__contains=search)).order_by('-watch_num')[:60].values('url', 'name', 'room_thumb', 'watch_num',
                                  'room_desc', 'platform_name')
    else:
        if type_name:
            if plat_name != "all":
                filter_info = PlatForm.objects.filter(platform_name=plat_name, channel_name=type_name).order_by('-watch_num')[:60].values('url', 'name', 'room_thumb', 'watch_num',
                                                                          'room_desc', 'platform_name')
            else:
                filter_info = PlatForm.objects.filter(channel_name=type_name).order_by('-watch_num')[:60].values('url', 'name', 'room_thumb', 'watch_num',
                                              'room_desc', 'platform_name')
        else:
            if plat_name != "all":
                filter_info = PlatForm.objects.filter(platform_name=plat_name).order_by('-watch_num')[:60].values('url', 'name', 'room_thumb', 'watch_num',
                                                                          'room_desc', 'platform_name')
            else:
                filter_info = PlatForm.objects.all().order_by('-watch_num')[:60].values('url', 'name', 'room_thumb', 'watch_num',
                                              'room_desc', 'platform_name')

    serialized_filter_info = json.dumps(list(filter_info), cls=DjangoJSONEncoder)

    name_dict = {
        'success': True,
        'data': {'page': 1,
                 'total': 1,
                 'liveList': serialized_filter_info}

    }
    return JsonResponse(name_dict)
