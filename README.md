# photoscan_project

Commands to run script:
```
$ photoscan -r /path/to/process_project.py --file /path/to/project.psx
```


##Data path format
```text
root/(ProjectName)Brazil2018 ---
      /(SiteName)UrubuRiver ---
          /(TransectName)CirclePlot1 ---
          /(ProjectFile)CirclePlot1.psx
          /ChunkImages1
               /IMG_XXXX.JPG ...
               /IMG_XXXX.JPG ...
               /IMG_XXXX.JPG ...
          /ChunkImages2
               /IMG_XXXX.JPG ...
              /IMG_XXXX.JPG ...
              /IMG_XXXX.JPG ...
          /(DEM)CirclePlot1.tif
          /(PointCloud)CirclePlot1.ply

```
