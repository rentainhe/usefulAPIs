import torch
import torch.nn as nn
import torch.nn.functional as F
import random
import numpy as np

'''
    Set a fixed Seed for training
'''
def set_seed(args):
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    if args.n_gpu > 0:
        torch.cuda.manual_seed_all(args.seed)