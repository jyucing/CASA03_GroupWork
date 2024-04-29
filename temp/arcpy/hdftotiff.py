# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 11:13:27 2022
 
@author: fkxxgis
"""
 
import os
import arcpy

hdf_file_path="D:/hdf/"
tif_file_path="E:/USS/CASA03_DigitalViz/GroupProject/data/temp/tiff/"

hdf_file_name_list=os.listdir(hdf_file_path)

for hdf_file in hdf_file_name_list:
    if os.path.isdir(hdf_file_path+hdf_file):
        file_name_temp=hdf_file
        hdf_file_name_list_new=os.listdir(hdf_file_path+hdf_file)
        for hdf_file in hdf_file_name_list_new:
            tif_file_name=hdf_file[8:23]+".tif"
            data=arcpy.ExtractSubDataset_management(hdf_file_path+file_name_temp+'/'+hdf_file,tif_file_path+tif_file_name,"0")
    else:
            tif_file_name=hdf_file[8:23]+".tif"
            data=arcpy.ExtractSubDataset_management(hdf_file_path+hdf_file,tif_file_path+tif_file_name,"0")
