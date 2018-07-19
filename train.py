#!/usr/bin/env python3

"""
Author      : Yukun Feng
Date        : 2018/07/01
Email       : yukunfg@gmail.com
Description : training
"""

import argparse
import opts
from utils.utils import get_logger
from onmt.decoders.decoder import StdRNNDecoder
from torch import nn


def parse_args():
    """ Parsing arguments """
    parser = argparse.ArgumentParser(
        description='preprocess.py',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    opts.preprocess_opts(parser)

    opt = parser.parse_args()
    #  torch.manual_seed(opt.seed)

    return opt


if __name__ == "__main__":
    opt = parse_args()
    logger = get_logger(opt.log_file)
    logger.info("It's a test")
    decoder_emb = nn.Embedding(100, 20)
    decoder = StdRNNDecoder(
        rnn_type="GRU",
        bidirectional_encoder=False,
        num_layers=1,
        hidden_size=30,
        embeddings=decoder_emb
    )
