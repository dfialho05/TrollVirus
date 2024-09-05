from pyperclip import copy
from keyboard import is_pressed
import time
from random import choice

def ctrlRand():
    data = {
        'text': [
            {
                '1': 'https://www.youtube.com/watch?v=L_jWHffIx5E',
                '2': 'https://www.youtube.com/watch?v=vm5NNWbf5w8',
                '3': 'https://www.youtube.com/watch?v=j2eY2ZUoDCo',
                '4': 'https://www.youtube.com/watch?v=astISOttCQ0',
                '5': 'https://www.youtube.com/watch?v=ZyhrYis509A',
                '6': 'https://www.youtube.com/watch?v=HlBYdiXdUa8',
                '7': 'https://www.youtube.com/watch?v=bG9z-atG7gc',
                '8': 'https://www.youtube.com/watch?v=Sy5iUYMtTO8',
                '9': 'https://www.youtube.com/watch?v=fOPGxQ4fgVw',
                '10': 'https://www.youtube.com/watch?v=Hb17uaaldwM',
                '11': 'https://www.youtube.com/watch?v=EDnIEWyVIlE',
                '12': 'https://www.youtube.com/watch?v=bCkCWnmAD-o',
                '13': 'https://www.youtube.com/watch?v=4KIlSKp9GDs',
                '14': 'https://www.youtube.com/watch?v=qw25BdjIh0o',
                '15': 'https://www.youtube.com/watch?v=V3_dH4NrAiY',
                '16': 'https://www.youtube.com/watch?v=-CEPcXyAjLE',
                '17': 'https://www.youtube.com/watch?v=r-8g_hIGNwM',
                '18': 'https://www.youtube.com/watch?v=wgTXYFcr1is',
                '19': 'https://www.youtube.com/watch?v=CH07sTbTSDU',
                '20': 'https://www.youtube.com/watch?v=9k6iDcpGByw',
                '21': 'https://www.youtube.com/watch?v=d1Sm_H2NDnQ',
                '22': 'https://www.youtube.com/watch?v=Y_LI2GDkSeE',
                '23': 'https://www.youtube.com/watch?v=8KhYhZtoHsc',
                '24': 'https://www.youtube.com/watch?v=6J2-c7cT1Wk'
            }
        ]
    }

    urls = list(data['text'][0].values())
    msg = choice(urls)

    while True:
        if is_pressed('ctrl+c') or is_pressed('ctrl+v'):
            msg = choice(urls)
            copy(msg)
            time.sleep(0.5)
            break