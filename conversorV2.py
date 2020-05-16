import csv
import sys
#import argparse
import xml.etree.cElementTree as ET
import argparse as args

parser = args.ArgumentParser(description='Analyzing commandline...')
parser.add_argument("Operacao", "--string",
                        required=True,
                        dest="arg_str",
                        type=str,
                        help="This is a required string argument.")

parsed_args = parser.parse_args()
print(parsed_args.blockfile)
