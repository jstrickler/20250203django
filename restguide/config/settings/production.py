from .base import *

DEBUG = False


# SECURITY WARNING: keep the secret key used in production secret! Read it from a file or from the environment
SECRET_KEY = '7s%3oj=t6ln40()r3-+-we180mvvry7$%@9_%#p6k3du4rcxzh'

# specify which domain names Django can serve (IOW the server the site is running on); this prevents HTTP host header
# attacks
ALLOWED_HOSTS = []  # put the site's hostnames here as  www.spam.com and spam.com

