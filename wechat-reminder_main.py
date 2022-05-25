#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : wechat-reminder_main.py
# Author            : Jing Mai <jingmai@pku.edu.cn>
# Date              : 05.25.2022
# Last Modified Date: 05.25.2022
# Last Modified By  : Jing Mai <jingmai@pku.edu.cn>

import os
import requests
import argparse


# Get environment variables
FT_SCKEY = os.environ.get('FT_SCKEY')

def main(args):
    url = f"https://sctapi.ftqq.com/{FT_SCKEY}.send"
    requests.post(url, data=vars(args))
 
if __name__ == '__main__':
    if FT_SCKEY is None:
        raise Exception('Environment variable FT_SCKEY is not set')
    parser = argparse.ArgumentParser(description='Send a message to WeChat.')
    parser.add_argument('--title', type=str, required=True, help='Title of the message. The maximum length is 32.')
    parser.add_argument('--desp', type=str, default="", help='Description of the message. The maximum length is 32KB.')
    args = parser.parse_args()
    main(args)
    