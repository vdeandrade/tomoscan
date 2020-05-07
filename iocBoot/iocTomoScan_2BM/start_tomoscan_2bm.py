# This script creates an object of type TomoScan13BM for doing tomography scans at APS beamline 13-BM-D
# To run this script type the following:
#     python -i start_tomoscan_13bm.py
# The -i is needed to keep Python running, otherwise it will create the object and exit
from tomoscan.tomoscan_2bm import TomoScan2BM
ts = TomoScan13BM(["../../db/tomoScan_settings.req","../../db/tomoScan_2BM_settings.req"], {"$(P)":"2bma:", "$(R)":"TomoScan:"})
