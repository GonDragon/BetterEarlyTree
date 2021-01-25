import os
import sys
import re
import csv


def run():
    moddir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    modname = os.path.basename(moddir)

    parts = {}

    # r = root, d = directories, f = files
    for r, _, f in os.walk(moddir):
        for file in f:
            if file.endswith(".cfg"):
                parts[file] = os.path.join(r, file)

    regex_modules = re.compile(r'([A-Z]+\n\{.*\})', flags=re.DOTALL)

    modules = []
    for _, v in parts.items():
        with open(v, 'r', encoding='utf-8', errors='ignore') as cfgFile:
            fileContent = ''.join(cfgFile.readlines())
            raw_modules = regex_modules.findall(fileContent)
            for raw_module in raw_modules:
                modules.append(Ksp_Module(raw_module))

    with open('_output/{0}_parts.csv'.format(modname), "w", newline='') as documentoSalida:
        parts_csv = csv.writer(
            documentoSalida, delimiter=',', quotechar='"')

        parts_csv.writerow(["name", "TechRequired"])

        for module in modules:
            if 'module' in module.attributes and module.attributes['module'] == 'Part':
                parts_csv.writerow([
                    module.attributes['name'].strip(), module.attributes['TechRequired'].strip()])


class Ksp_Module:
    _REGEX_MODULES = re.compile(r'([A-Z]+)\s+\{(.*)\}', flags=re.DOTALL)
    _REGEX_ATTRIBUTES = re.compile(r'([A-Za-z]+)\s=\s(.*)')

    def __init__(self, string):
        modules = self._REGEX_MODULES.search(string)
        self.name = modules.group(1)
        self.attributes = {}
        self.content = modules.group(2)

        regex_attributes = self._REGEX_ATTRIBUTES.findall(modules.group(2))
        for k, v in regex_attributes:
            if not k in self.attributes:
                self.attributes[k] = v


run()
