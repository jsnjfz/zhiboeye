from django.shortcuts import render
from django.views.generic.base import View
from .models import PlatForm, ChannelDict

# Create your views here.


class IndexView(View):
    def get(self, request):
        all_info = PlatForm.objects.all().order_by('-watch_num')[:30]
        all_channel_type = ChannelDict.objects.all()
        return render(request, "index.html", {
            "all_info":all_info,
            "all_channel_type":all_channel_type
        })