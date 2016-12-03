# -*- encoding: utf-8 -*-

import os
import gzip

from .. import resource_path


def download_database():
    target = os.path.join(resource_path, "veekun-pokedex.sqlite")
    source = os.path.join(resource_path, "veekun-pokedex.sqlite.gz")
    
    if os.path.isfile(target):
        return

    with gzip.open(source, "rb") as in_file:
        s = in_file.read()

    with open(target, "wb") as f:
        f.write(s)
