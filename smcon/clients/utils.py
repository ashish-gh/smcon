import os
import json

from requests.models import Request
from .errors import ClientConnectionError

def load_json(data):        
    if isinstance(data, Request):
        try:
            data = data.text
        except:
            data = ""
    elif isinstance(data, str):
        # do something else
        data = ""
    return data


def load_respose(data):        
    if isinstance(data, Request):
        try:
            data = data.text
        except:
            data = ""
    elif isinstance(data, str):
        # do something else
        data = ""
    return data
