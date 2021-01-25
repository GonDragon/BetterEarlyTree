#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import csv


DEF_TEMPLATE = "@PART[{0}]:NEEDS[{1}]:AFTER[BetterEarlyTree]\n{{\n   @TechRequired = {2}\n}}"


def main():

    # dic[mod] = [{techRequired : [part1, part2, ...]}, ...]
    parts_from_mod = {}

    with open('newPartArrangement.csv', "r") as documento:
        parts = csv.reader(documento, delimiter=',', quotechar='"')

        next(parts, None)  # skip the headers
        for name, tech, mod in parts:
            if not mod in parts_from_mod:
                parts_from_mod[mod] = {}
            if not tech in parts_from_mod[mod]:
                parts_from_mod[mod][tech] = []
            parts_from_mod[mod][tech].append(name)

    for mod in parts_from_mod:
        with open('_output/patches/BET-{0}.cfg'.format(mod), "w", newline='') as outputCfg:
            for tech, names in parts_from_mod[mod].items():
                outputCfg.write(DEF_TEMPLATE.format(
                    '|'.join(names), mod, tech) + '\n\n')


if __name__ == "__main__":
    main()
