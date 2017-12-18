import os, sys
import argparse

def main():
    os.chdir("../src") # change to app directory

    parser = argparse.ArgumentParser(description="Generate pano from image files")
    parser.add_argument('files', type=str, nargs='+', help="Files to process")
    args = parser.parse_args()

    for filepath in args.files:
        targetList = ""
        targets = os.listdir(str(filepath))
        for target in targets:
            targetList += filepath + "/" + target + " "
        finalCmd = "./image-stitching " + targetList
        print(finalCmd)
        os.system(finalCmd)

if __name__ == '__main__':
    main()
