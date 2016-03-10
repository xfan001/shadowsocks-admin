import socket
import string
import random

MANAGE_PASS = 'lifan_mmd'
MANAGE_BIND_IP = '127.0.0.1'
MANAGE_PORT = 23333


def del_server(port, passwd):
    """
    delete a server
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    command = '%s:%s:%s:%s' % (MANAGE_PASS, port, passwd, 0)
    s.sendto(command, (MANAGE_BIND_IP, MANAGE_PORT))
    s.close()


def add_server():
    """
    add new server, return (port, password)
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    new_port = get_free_port()
    new_passwd = gen_password()
    command = '%s:%s:%s:%s' % (MANAGE_PASS, new_port, new_passwd, 1)
    s.sendto(command, (MANAGE_BIND_IP, MANAGE_PORT))
    s.close()
    return (new_port, new_passwd)


def get_free_port():
    """
    get avaliable port in system
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", 0))
    port = s.getsockname()[1]
    s.close()
    return port


def gen_password(length=8):
    """
    generate random password, use the arg length
    """
    chars_set = string.ascii_letters + string.digits
    return ''.join([random.choice(chars_set) for i in range(length)])


def get_init_flow():
    return 10*1024*1024*1024