# photoscan_project
 
## Steps:
1. Command line launch $photoscan
2. Start a new project
3. Create new chunks, one for each drone flight "pass" over site.
4. Load pictures (cams) into appropriate chunks by flight time. Check that all photos in a chunk should be from the same drone flight "pass."
4.5 Manually remove outlier (take-off, landing) cams that do not align
5. Open 'Tool->Camera Calibration'
6. Set type to "Precalibrated".
7. Check "Fix calibration"
8. Enter values for f:....p4: from calibration table on Github
9. Save these parameters. You can call them again in future projects.
10. If using multiple chunks, check to see if calibration parameters are the same for all chunks. Make changes as needed so all are the same.
11. Save project and close photoscan
12. Change to /opt directory to run process by:   $ cd /opt/photoscan-pro
13. Run project with commands below


$$$TIPS$$$
You may have to execute the files from this directory: /opt/photoscan-pro/photoscan.sh

Two strategies for running tests:
a) Select only a few photos that overlap (~7-10)
or
b) in .py file change run settings (in your personal copy, not on github)

### camera calibration calculated adjusted
|Camera |Calibration|||  
|---|---|---|---|  
|f:| 3516.110433	|	 |	 |  
|cx:|	-49.2002547|	b1:|0	|  
|cy:|	259.0410213|	b2:|0	|  
|k1:|	0.0540362|	p1:| -0.012976|  
|k2:|	-2.56097|	p2:| 0.00237692|  
|k3:|	5.06261|	p3:|0	|  
|k4:| 0	|	p4:|0	|  








Commands to run script:
```bash
$ ./photoscan.sh -r /path/to/process_project.py --file /path/to/project.psx
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
