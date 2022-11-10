#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import argparse
import json
import csv

sys.path.append("..")

def add_args():
    parser = argparse.ArgumentParser(description='Generates a summary of the data contained in a Tweet dataset.')
    parser.add_argument('-i', '--infile', metavar='', required=True, help='Filename for the input JSON file')
    parser.add_argument('-o', '--outfile', metavar='', default='output', help='Filename for the resulting output. Default is "output.csv"')
    return parser.parse_args()

def convert(infile, outfile):
    sys.stdout.write('Loading JSON file...'+"\n")
    sys.stdout.flush()

    with open(infile, "r") as f:
        data = json.load(f)

    sys.stdout.write('Converting JSON file to CSV...'+"\n")
    sys.stdout.flush()

    with open(outfile + ".csv", "w", newline="") as f:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for tweet in data:
            writer.writerow(tweet)

    sys.stdout.write('Succesfully wrote file to ' + outfile + '.csv!'+"\n")
    sys.stdout.flush()

def main(args):
    convert(args.infile, args.outfile)

if __name__== "__main__":
    args = add_args()
    main(args)