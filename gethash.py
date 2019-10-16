from __future__ import unicode_literals

import os
import sys

from tqdm import tqdm
from instabot import Bot  # noqa: E402

bot = Bot()
bot.login(username="alpha_test.me", password="dado1234")

def dispositions(l):
    from itertools import permutations
#Disposition - generating words from tags
    print("Generating dispositions...")
    res = []
    res += [a for a in l]
    length = len(l)
    num = 2
    while num <= length:
        p = list(permutations(l, num))
        res += [" ".join(c) for c in p]
        num += 1
    print("Generated {} dispositions".format(len(res)))
    return res
# Sadrzi tagove koje ce kombinirati
hash = ["nature", "social"]

# Tags empty dictionary
tags = {}
# Loop, take values from disposition, search tags and store them
for i in tqdm(dispositions(hash[0:])):
    bot.api.search_tags(i)
    res = bot.api.last_json
    for result in res["results"]:
        tags[result["name"]] = result["media_count"]
sorted_by_value = sorted(tags.items(), key=lambda kv: kv[1], reverse=True)

bot.logger.info("Found {} hashtags".format(len(sorted_by_value)))
for tag in sorted_by_value:
    if tag[1] < 1000:
        color = "34"
    elif tag[1] < 10000:
        color = "35"
    elif tag[1] < 100000:
        color = "31"
    elif tag[1] < 1000000:
        color = "33"
    elif tag[1] < 10000000:
        color = "32"
    elif tag[1] < 100000000:
        color = "36"
    else:
        color = "30;46"
    print(
        "\033[{color}mmedias: {count:,} -> TAG: {tag}\033[0m".format(
            color=color, tag=tag[0], count=tag[1]
        )
    )