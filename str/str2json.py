#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


class Solution(object):

    def json_dump(self, jstr):
        ret_json = ''
        next_line = '\n'
        next_tab = '\t'
        next_blank = ' '
        count_left = 0
        for i in jstr:
            other = ''
            if i == '{':
                count_left += 1
                other = next_line + next_tab * count_left
                ret_json += i + other
            elif i == ',':
                other = next_line + next_tab * count_left
                ret_json += i + other
            elif i == ':':
                other = next_blank
                ret_json += i + other
            elif i == '[':
                count_left += 1
                other = next_line + next_tab * count_left
                ret_json += i + other
            elif i == ']':
                count_left -= 1
                other = next_line + next_tab * count_left
                ret_json += other + i
            elif i == '}':
                count_left -= 1
                other = next_line + next_tab * count_left
                ret_json += other + i
            else:
                ret_json += i

        return ret_json


if __name__ == '__main__':
    str_json = '{"employees":[{"firstName":"Bill","lastName":{"Gates":"Any"}},\
        {"firstName":"George","lastName":"Bush"},\
        {"firstName":"Thomas","lastName":"Carter"}]}'
    print json.dumps(eval(str_json), indent=8)
    s_obj = Solution()
    print s_obj.json_dump(str_json)
