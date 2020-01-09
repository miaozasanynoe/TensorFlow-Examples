from __future__ import division, print_function, absolute_import

import collections
import os
import random
import urllib
import zipfile

import numpy as np
import tensorflow as tf
#训练参数
learning_rate = 0.1
batch_size = 128
num_steps = 3000000
display_step = 10000
eval_step = 200000
#