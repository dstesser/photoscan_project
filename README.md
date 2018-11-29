# photoscan_project


Commands to run script:
```bash
$ photoscan -r /path/to/process_project.py --file /path/to/project.psx
```
Run command in tmux terminal window to run in background.

```bash
$ tmux
```

Start process and exit using ```Cntrl-D```. To rejoin process use:

```bash
$ tmux attach-session
```


## Data path format
```text
root/(ProjectName)Brazil2018 ---
      /(SiteName)UrubuRiver ---
          /(TransectName)CirclePlot1 ---
                /(ProjectFile)CirclePlot1.psx
                /FlightPeriodImages1 <-- Only if moved in building chunks,
                    /IMG_XXXX.JPG ...
                    /IMG_XXXX.JPG ...
                    /IMG_XXXX.JPG ...
                /FlightPeriodImages2 <-- Only if moved in building chunks,
                    /IMG_XXXX.JPG ...
                    /IMG_XXXX.JPG ...
                    /IMG_XXXX.JPG ...
                /(DEM)CirclePlot1.tif
                /(PointCloud)CirclePlot1.ply

```
