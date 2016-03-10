#coding:utf-8
from __future__ import division
from datetime import datetime

from django.conf import settings
from django.contrib import admin
from .models import SSInfo
from django.contrib.auth.models import User
from django.contrib.admin import DateFieldListFilter

from ssmanagement.utils import get_init_flow
from  send_mail import send_info_email


@admin.register(SSInfo)
class SSInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'contact_info', 'user_name', 'port', 'passwd',
                    'get_last_alive_time',
                    'get_upload', 'get_download', 'amount_used',
                    'get_transfer_enable', 'switch', 'enable')
    list_filter = (DateFieldListFilter,)
    ordering = ['id']
    search_fields = ['contact_info', 'user_name',]
    actions = ['reset_traffic', 'send_email']

    def get_last_alive_time(self, obj):
        return datetime.fromtimestamp(obj.t).strftime('%Y/%m/%d %H:%M:%S')
    get_last_alive_time.short_description = u'Last-Alive-Time'

    def get_upload(self, obj):
        return self._get_readable_flow(obj.u)
    get_upload.short_description = u'Upload'

    def get_download(self, obj):
        return self._get_readable_flow(obj.d)
    get_download.short_description = u'Download'

    def amount_used(self, obj):
        return self._get_readable_flow(obj.u+obj.d)
    amount_used.short_description = 'Used'

    def get_transfer_enable(self, obj):
        return self._get_readable_flow(obj.transfer_enable)
    get_transfer_enable.short_description = u'Limit'

    def _get_readable_flow(self, value):
        value = long(value)
        if value < 1024:
            return '%sB' % value
        elif value < 1024*1024:
            return '%sK' % (value//1024)
        elif value < 1024*1024*1024:
            return '%.2fM' % (value/1024/1024)
        else:
            return '%.2fG' % (value/1024/1024/1024)


    #######ACTIONS############
    def reset_traffic(self, request, queryset):
        rows_updated = queryset.update(u=0, d=0)
        if rows_updated == 1:
            message_bit = '1 account has been'
        else:
            message_bit = '%s accounts have been' % rows_updated
        self.message_user(request, "%s reset successfully." % message_bit)
    reset_traffic.short_description = u'流量清零'

    def send_email(self, request, queryset):
        for obj in queryset:
            info_dict = {
                'ssobj': obj,
                'ipv4': settings.IPV4,
                'ipv6': settings.IPV6
            }
            if '@' in obj.contact_info:
                send_info_email(obj.contact_info, info_dict)
            else:
                self.message_user(request, 'not email format')
                break
        else:
            self.message_user(request, 'send email successfully')
    send_email.short_description = u'发邮件告知信息'