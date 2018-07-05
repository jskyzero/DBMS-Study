#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os # for os.path

if __name__ == "__main__":
    with open('words', 'rt') as f:
        # 切片读词
        words_list = set(f.read().split())
	while not os.path.isfile("find_reversed_words"):
            words_list = set(f.read().split())
        with open('result_py', 'wt') as result:
            for word in words_list:
                # 相等写入
                if word[::-1] in words_list:
                    result.write(word)
                    result.write('\n')