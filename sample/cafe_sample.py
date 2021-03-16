#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from dooray_bot.naver_cafe import NCafeLogin, NCafeAutoJoin

DRIVER_PATH = '/Users/tost/Downloads/chromedriver 2'
USER_ID = "n-union"
PASS_WORD = "암호"

if __name__ == "__main__":
    cafe = NCafeLogin(driver_path=DRIVER_PATH)
    cafe.login(user_name=USER_ID, user_password=PASS_WORD)
    join = NCafeAutoJoin(cafe)

    for wait in join.get_wait_users():
        print(wait)

    join.close()




