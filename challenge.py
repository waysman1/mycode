#!/usr/bin/env python3

def print_length(list_o_words):
    s_count = 0
    m_count = 0
    l_count = 0
    for word in list_o_words:
        if len(word) < 5:
            s_count += 1
        elif len(word) < 10:
            m_count += 1
        else:
            l_count += 1

print(f'There are {s_count} short words, {m_count} medium word, and {l_count} lond words')

example_list = ['banana', 'blueberries', 'nuts', 'acorns']
print_length(example_list)


