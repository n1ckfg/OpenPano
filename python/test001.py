import os
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Generate pano from image files")
    parser.add_argument('files', type=str, nargs='+', help="Files to process")
    args = parser.parse_args()

    for filename in args.files:
        print(os.listdir("."))

if __name__ == '__main__':
    main()
