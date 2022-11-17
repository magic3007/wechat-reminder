#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : wechat-reminder_main.py
# Author            : Jing Mai <jingmai@pku.edu.cn>
# Date              : 05.25.2022
# Last Modified Date: 05.25.2022
# Last Modified By  : Jing Mai <jingmai@pku.edu.cn>

import os
import argparse
from pypushdeer import PushDeer


# Get environment variables
PUSHDEER_KEY = os.environ.get("PUSHDEER_KEY")


def main(args):
    for key in PUSHDEER_KEY.split(","):
        pushdeer = PushDeer(pushkey=key)
        pushdeer.send_text(args.title, desp=args.desp)


if __name__ == "__main__":
    if PUSHDEER_KEY is None:
        raise Exception("Environment variable PUSHDEER_KEY is not set")
    parser = argparse.ArgumentParser(description="Send a message to WeChat.")
    parser.add_argument(
        "--title", type=str, required=True, help="Title of the message."
    )
    parser.add_argument(
        "--desp", type=str, default="", help="Description of the message."
    )
    args = parser.parse_args()
    main(args)
