import os
import sys
import argparse

import PhotoScan

def main():

    result_file = args.file.replace('.psx', '_result.psx')

    doc = PhotoScan.app.document
    doc.open(args.file)
    for chunk in doc.chunks:
        chunk.matchPhotos(accuracy=PhotoScan.HighestAccuracy, generic_preselection=True, reference_preselection=False)
        chunk.alignCameras()
    doc.mergeChunks(doc.chunks, merge_dense_clouds=True)
    doc.chunk = doc.chunks[-1]
    print(doc.chunk)
    doc.chunk.buildDepthMaps(quality=PhotoScan.HighQuality, filter=PhotoScan.AggressiveFiltering)

    doc.chunk.buildDenseCloud()
    doc.save(result_file)

    doc.chunk.buildDem()
    doc.save(result_file)
    # save output

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', default=None, help='path to project file')
    args = parser.parse_args()
    main()