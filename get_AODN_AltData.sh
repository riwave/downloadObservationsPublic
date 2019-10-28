#!/bin/bash

# http://thredds.aodn.org.au/thredds/catalog/IMOS/SRS/Surface-Waves/Wave-Wind-Altimetry-DM00/catalog.html
fname=http://thredds.aodn.org.au/thredds/fileServer/IMOS/SRS/Surface-Waves/Wave-Wind-Altimetry-DM00
DIR=/media/monet/public/satellite/altimeter/AODN/JASON3 

# JASON-3 JASON-2 CRYOSAT-2 JASON-1 HY-2 SARAL SENTINEL-3A ENVISAT ERS-1 ERS-2 GEOSAT GFO TOPEX

s=JASON-3; h="S"
for lon in `seq -f "%03g" 0 20 340`; do
  for lat in `seq -f "%03g" 20 20 80`; do
    for adlat in `seq -f "%03g" 0 19`; do
      lat2=(`expr $lat - $adlat`)
      for adlon in `seq -f "%03g" 0 19`; do
        lon2=(`expr $lon + $adlon`)
        echo IMOS_SRS-Surface-Waves_MW_${s}_FV02_"$(printf "%03d" $lat2)"${h}-"$(printf "%03d" $lon2)"E-DM00.nc >> listDownloaded_${s}.txt
        wget -l1 -H -t1 -nd -N -np -erobots=off --tries=5 $fname/${s}/${lat}${h}_${lon}E/IMOS_SRS-Surface-Waves_MW_${s}_FV02_"$(printf "%03d" $lat2)"${h}-"$(printf "%03d" $lon2)"E-DM00.nc -O $DIR/IMOS_SRS-Surface-Waves_MW_${s}_FV02_"$(printf "%03d" $lat2)"${h}-"$(printf "%03d" $lon2)"E-DM00.nc
      done
    done
  done
done
echo " " >> listDownloaded_${s}.txt
echo "Southern Hemisphere OK, "${s}"   " >> listDownloaded_${s}.txt
echo " " >> listDownloaded_${s}.txt

find $DIR -empty -type f -delete

h="N"
for lon in `seq -f "%03g" 0 20 340`; do
  for lat in `seq -f "%03g" 0 20 80`; do
    for adlat in `seq -f "%03g" 0 19`; do
      lat2=(`expr $lat + $adlat`)
      for adlon in `seq -f "%03g" 0 19`; do
        lon2=(`expr $lon + $adlon`)
        echo IMOS_SRS-Surface-Waves_MW_${s}_FV02_"$(printf "%03d" $lat2)"${h}-"$(printf "%03d" $lon2)"E-DM00.nc >> listDownloaded_${s}.txt
        wget -l1 -H -t1 -nd -N -np -erobots=off --tries=5 $fname/${s}/${lat}${h}_${lon}E/IMOS_SRS-Surface-Waves_MW_${s}_FV02_"$(printf "%03d" $lat2)"${h}-"$(printf "%03d" $lon2)"E-DM00.nc -O $DIR/IMOS_SRS-Surface-Waves_MW_${s}_FV02_"$(printf "%03d" $lat2)"${h}-"$(printf "%03d" $lon2)"E-DM00.nc
      done
    done
  done
done
echo " " >> listDownloaded_${s}.txt
echo "Northern Hemisphere OK, "${s}"   " >> listDownloaded_${s}.txt
echo " " >> listDownloaded_${s}.txt

find $DIR -empty -type f -delete


