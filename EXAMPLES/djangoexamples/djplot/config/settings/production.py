from .base import *

DEBUG = False


# SECURITY WARNING: keep the secret key used in production secret! Read it from a file or from the environment
SECRET_KEY = 'k7%bhlq12gy&h+%&py)7+e1@_8x+q$087@i^-ss7)ndm^1=z9w'

# specify which domain names Django can serve (IOW the server the site is running on); this prevents HTTP host header
# attacks
ALLOWED_HOSTS = []  # put the site's hostnames here as  www.spam.com and spam.com

