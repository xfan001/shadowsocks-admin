#encoding=utf-8
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

import time

from utils import gen_password, get_free_port, get_init_flow, del_server

def get_timestamp():
    return int(time.time())

class SSInfo(models.Model):
    id = models.AutoField(primary_key=True)
    contact_info = models.CharField(max_length=30, blank=True, null=True)
    user_name = models.CharField(max_length=30, blank=True, null=True)
    passwd = models.CharField(max_length=16, default=gen_password)
    t = models.IntegerField(default=get_timestamp())
    u = models.BigIntegerField(default=0)
    d = models.BigIntegerField(default=0)
    transfer_enable = models.BigIntegerField(default=get_init_flow)
    port = models.IntegerField(unique=True, default=get_free_port)
    switch = models.BooleanField(default=True)
    enable = models.BooleanField(default=True)

    class Meta:
        db_table = "user"
        verbose_name = 'Shadowsocks'
        verbose_name_plural = 'Shadowsocks'

    def __unicode__(self):
        return '%s(%s)' % (self.user_name, self.contact_info)


@receiver(post_save, sender=SSInfo)
def disable_callback(sender, instance, created, **kwargs):
    if not instance.enable:
        del_server(instance.port, instance.passwd)