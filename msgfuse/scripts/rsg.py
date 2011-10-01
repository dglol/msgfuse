import sys
import random

charset = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'

def generate():
    strlist = []
    for i in range(5):
        strlist.append(random.choice(charset))
    return ''.join(strlist)
