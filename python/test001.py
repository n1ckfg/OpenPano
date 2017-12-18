import os
import sys
import argparse

def main():
    os.listdir(".")

    parser = argparse.ArgumentParser(description="Convert Norman .json")
    #parser.add_argument('--strokes', action='store_true', help="Dump the strokes")
    #parser.add_argument('--metadata', action='store_true', help="Dump the metadata")
    parser.add_argument('files', type=str, nargs='+', help="Files to examine")

    args = parser.parse_args()
    #if not (args.strokes or args.metadata):
        #print "You should pass at least one of --strokes or --metadata"

    for filename in args.files:
        save_gp(filename)

if __name__ == '__main__':
    main()