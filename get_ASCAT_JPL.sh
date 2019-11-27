#!/bin/bash

# ASCAT scaterometer
sn=https://podaac-opendap.jpl.nasa.gov/opendap/allData/ascat/preview/L2/metop_a/25km

for year in `seq -f "%03g" 2017 1 2019`; do
  for day in `seq -f "%03g" 1 366`; do
    fname=${sn}/${year}/${day}/
    echo "Dowloading $fname"
    wget -r -l1 -H -t1 -nd -N -np -A.nc.gz -erobots=off $fname
  done
done
# ----------------------------
