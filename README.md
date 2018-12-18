# photoscan_project
## camera calibration
 

|Camera |abc|abc|abc|  
|---|---|---|---|  
|f:| 3516.110433	|	Calculated|	adjusted|  
|cx:|	-49.2002547|	b1:|0	|  
|cy:|	259.0410213|	b2:|0	|  
|k1:|	0.0540362|	p1:| -0.012976|  
|k2:|	-2.56097|	p2:| 0.00237692|  
|k3:|	5.06261|	p3:|0	|  
|k4:| 0	|	p4:|0	|  








Commands to run script:
```bash
$ photoscan -r /path/to/process_project.py --file /path/to/project.psx
```
Run command in tmux terminal window to run in background.

```bash
$ tmux
```

Start process and exit using ```Ctrl-B + D```. To rejoin process use:

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
