# -*- coding: cp936 -*-
import arcpy

# 使用原始字符串设置工作路径
arcpy.env.workspace = r"E:\USS\CASA03_DigitalViz\GroupProject\data\temp\tiff84\tiff_global"

# 遍历所有TIF
rasterlist1 = arcpy.ListRasters("*", "tif")
print(rasterlist1)

# 检查rasterlist1是否为None
if rasterlist1 is None:
    print("No raster files found in the directory.")
else:
    # 转换
    for raster in rasterlist1:
        print(raster)
        inRaster = raster
        # 以原文件名输出至另一个文件夹
        out = r"E:\USS\CASA03_DigitalViz\GroupProject\data\temp\temp_points\{}".format(raster)
        arcpy.RasterToPoint_conversion(inRaster, out, "Value")
        print("Change done!")

print("Well done!")
