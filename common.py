import requests
import json
import logging
import sys

f = open("conf.json","r")
conf = json.load(f)
apiEndPoint = conf["api_endpoint"]

def setup_custom_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler('log.txt', mode='w')
    handler.setFormatter(formatter)
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(screen_handler)
    return logger

logger = setup_custom_logger('dob-app')

def time_left_for_next_birthday(dateOfBirth, unit):
   logger.info('Query parameters passed to the api: %s  %s ', dateOfBirth, unit )
   url = apiEndPoint+"?dateofbirth="+dateOfBirth+"&unit="+unit
   headers = {'Accept':'*/*'}
   response = requests.get(url, headers=headers)
   #print(response.status_code)
   #print(response)
   logger.debug(response.content)
   return response
