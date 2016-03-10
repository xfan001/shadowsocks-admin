#encoding=utf-8

import os, sys
import subprocess
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from ssmanagement.models import SSInfo
import logging

def main():
    logging.log(logging.INFO, '*****\ntraffic clearing\n')
    SSInfo.objects.exclude(id=1).update(u=0, d=0)
    subprocess.call('supervisorctl restart shadowsocks'.split())
    logging.log(logging.INFO, 'done!\n*****')

if __name__ == '__main__':
    main()