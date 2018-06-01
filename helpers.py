# https://github.com/spro/char-rnn.pytorch

import unidecode
import time
import math
import torch


def read_file(filename):
    """Reading and un-unicode-encoding data"""
    file = unidecode.unidecode(open(filename).read())
    return file, len(file)


def char_tensor(string):
    """Turning a string into a tensor"""
    tensor = torch.zeros(len(string)).long()
    for c in range(len(string)):
        try:
            tensor[c] = string.printable.index(string[c])
        except:
            continue
    return tensor


# Readable time elapsed
def time_since(since):
    s = time.time() - since
    m = math.floor(s / 60)
    s -= m * 60
    return '%dm %ds' % (m, s)
