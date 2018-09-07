# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

import requests

width_window = 1000 # content presentation width

### Helpers: Presentation system

### Validate content to show, to verify that we can show something online, if not, we show the alternative
def show_content(content, alternative, url_check):
    HTML_to_Render = ""
    if check_connection(url_check):
        HTML_to_Render = content
    else:
        HTML_to_Render = alternative

    return HTML_to_Render

def check_connection(URL):
    try:
        r = requests.get(URL)
        if r.status_code == 200:
            return 1
        else:
            return 0
    except:
        return 0

## Wrappers ober the HTML tags
#  
def html_video(url, width=width_window):
    return f'<video src="videos/{url}" width="{width} px" autoplay loop muted style="display: block;margin-left: auto; margin-right: auto;" ></video>'

def html_video_stop(url, width=width_window):
    return f'<video src="videos/{url}" width="{width} px" autoplay muted style="display: block;margin-left: auto; margin-right: auto;" ></video>'

def html_video_pause_stop(url, width=width_window):
    return f'<video src="videos/{url}" width="{width} px" controls muted style="display: block;margin-left: auto; margin-right: auto;" ></video>'

def html_img(url, width=width_window):
    return f'<img src="images/{url}" width="{width} px" class="jp-mod-unconfined" style="display: block;margin-left: auto; margin-right: auto;" ></img>'

def html_iframe(url, width=width_window):
    return f'<iframe src="{url}" width="{width} px" height="800 px" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen class="jp-mod-unconfined" style="display: block;margin-left: auto; margin-right: auto;" ></ifr>'

def html_link(content, link):
    return f'<a href="{link}" target="_blank" class="jp-mod-unconfined" class="jp-mod-unconfined" style="display: block;margin-left: auto; margin-right: auto;" >{content}</a>'
