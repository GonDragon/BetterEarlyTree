#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import csv


DEF_TEMPLATE = "@PART[{0}]:NEEDS[{1}]:AFTER[BetterEarlyTree]\n{{\n   @TechRequired = {2}\n   {3}\n}}"


def main():

    # dic[mod] = [{techRequired : [(part1, price1), (part2, price2), ...]}, ...]
    parts_from_mod = {}

    with open('newPartArrangement.csv', "r") as documento:
        parts = csv.reader(documento, delimiter=',', quotechar='"')

        next(parts, None)  # skip the headers
        for name, tech, mod, price in parts:
            if not mod in parts_from_mod:
                parts_from_mod[mod] = {}
            if not tech in parts_from_mod[mod]:
                parts_from_mod[mod][tech] = []
            parts_from_mod[mod][tech].append((name, price))

    for mod in parts_from_mod:
        with open('_output/patches/BET-{0}.cfg'.format(mod), "w", newline='') as outputCfg:
            outputCfg.write('// This section is Script-generated\n\n')
            for tech, parts in parts_from_mod[mod].items():
                for part in parts:
                    name, price = part
                    final_price = ''
                    if price.isnumeric():
                        final_price = '@entryCost = ' + price
                    outputCfg.write(DEF_TEMPLATE.format(
                        name, mod, tech, final_price) + '\n\n')


if __name__ == "__main__":
    main()
