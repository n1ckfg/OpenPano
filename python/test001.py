import os
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Generate pano from image files")
    parser.add_argument('files', type=str, nargs='+', help="Files to process")
    args = parser.parse_args()

    for filepath in args.files:
        targetList = ""
        targets = os.listdir(str(filepath))
        for target in targets:
            targetList += filepath + "/" + target + " "
        os.system("./../src/image-stitching " + targetList)

if __name__ == '__main__':
    main()
