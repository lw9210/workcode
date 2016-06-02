#!/usr/bin/env python
# -*- coding:utf-8 -*-

def WordPattern(pattern, string):
    str_list = string.split(" ")
    if len(pattern) != len(str_list):
        return False
    dict_pattern = {}
    str_pattern = {}
    for i in range(len(pattern)):
        if not dict_pattern.get(pattern[i]):
            dict_pattern[pattern[i]] = str_list[i]
        if not str_pattern.get(str_list[i]):
            str_pattern[str_list[i]] = pattern[i]
        if dict_pattern[pattern[i]] != str_list[i] or str_pattern[str_list[i]] != pattern[i]:
            return False
    return True

if __name__ == "__main__":
    pattern = "abba"
    string = "boy girl girl boy"
    rtn = WordPattern(pattern, string)
    print rtn
    pattern = "abbb"
    string = "man man woman woman"
    rtn = WordPattern(pattern, string)
    print rtn
