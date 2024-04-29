# -*- coding: cp936 -*-
# Name: RasterToPoint_Ex_02.py
# Description: Converts a raster dataset to point features.
# Requirements: None

# Import system modules
import arcpy
from arcpy import env
import glob
import os

# Set environment settings
env.workspace = "E:/USS/CASA03_DigitalViz/GroupProject/data/temp/tiff84/tiff_global/"

inPath = 'E:/USS/CASA03_DigitalViz/GroupProject/data/temp/tiff84/tiff_global/'
outPath = 'E:/USS/CASA03_DigitalViz/GroupProject/data/temp/temp_points/'

filename_list = os.listdir(inPath)

for tiff_file in filename_list:
    full_tiff_path = os.path.join(inPath, tiff_file)
    if os.path.isfile(full_tiff_path):  # 确保是文件
        shp_file_name = tiff_file[:15] + ".shp"  # 确保这里的字符串切片是正确的
        full_shp_path = os.path.join(outPath, shp_file_name)
        print("Trying to convert")  # 打印路径以供检查
        try:
            arcpy.RasterToPoint_conversion(full_tiff_path, full_shp_path, "grid_code")
            print("Conversion successful")
        except arcpy.ExecuteError as e:  # 捕获ArcPy执行错误
            print("Conversion failed")
        except Exception as e:  # 捕获其他所有错误
            print("An error occurred")
