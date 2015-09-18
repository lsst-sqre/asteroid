import getpass
from pprint import pprint
from sys import stdin, stdout

from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver as libcloud_get_driver
from libcloud.security import VERIFY_SSL_CERT


VERIFY_SSL_CERT = False


def get_driver(username, password):
    OpenStack = libcloud_get_driver(Provider.OPENSTACK)
    return OpenStack(
        key=username,
        secret=password,
        ex_tenant_name='LSST',
        ex_force_auth_url='http://nebula.ncsa.illinois.edu:5000/v2.0/tokens/',
        ex_force_auth_version='2.0_password')    


def prompt_username():
    username = getpass.getuser()
    print('Username [%s] ⇝ ' % (username), end='', flush=True)
    _input = stdin.readline()
    if _input.strip():
        return _input.strip()
    else:
        return username
    

def prompt_and_get_driver():
    return get_driver(prompt_username(),
                      getpass.getpass(prompt='Password ⇝ '))


def main():
    driver = prompt_and_get_driver()
    pprint(driver.list_sizes())
    pprint(driver.list_images())
    pprint(driver.list_nodes())


if __name__ == '__main__':
    main()
