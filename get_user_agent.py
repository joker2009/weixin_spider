#!/usr/bin/python
# -*- coding:utf-8 -*-

import random
from user_agent_list import user_agent_list


class UserAgent(object):
    def __init__(self):
        self.USER_AGENT_LIST = user_agent_list()

    def get_user_agent(self):
        user_agent = random.choice(self.USER_AGENT_LIST)
        return user_agent


if __name__ == '__main__':
    ua = UserAgent()
    random_ua = ua  # .get_user_agent()
    print(random_ua)

