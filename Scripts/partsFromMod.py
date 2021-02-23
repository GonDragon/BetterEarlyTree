import os
import sys
import re
import csv
from KSPModule import Reader


def run():
    moddir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    modname = os.path.basename(moddir)

    files = {}

    # r = root, d = directories, f = files
    for r, _, f in os.walk(moddir):
        for file in f:
            if file.endswith(".cfg"):
                files[file] = os.path.join(r, file)

    parts = [["name", "TechRequired"]]

    for _, v in files.items():
        with open(v, 'r', encoding='utf-8-sig') as cfgFile:
            try:
                reader = Reader(cfgFile)
            except:
                print(v)
                continue
            for module in reader:
                if module.type.upper() == 'PART' and module.has_attribute("TechRequired"):
                    try:
                        parts.append([module.get_attribute("name"), module.get_attribute(
                            "TechRequired")])
                    except:
                        print("Unexpected error on module:\n{}".format(str(module)))

    with open('_output/{0}_parts.csv'.format(modname), "w", newline='') as documentoSalida:
        csv.writer(documentoSalida, delimiter=',',
                   quotechar='"').writerows(parts)


run()
