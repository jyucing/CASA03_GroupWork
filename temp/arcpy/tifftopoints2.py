# -*- coding: cp936 -*-
import arcpy

# ʹ��ԭʼ�ַ������ù���·��
arcpy.env.workspace = r"E:\USS\CASA03_DigitalViz\GroupProject\data\temp\tiff84\tiff_global"

# ��������TIF
rasterlist1 = arcpy.ListRasters("*", "tif")
print(rasterlist1)

# ���rasterlist1�Ƿ�ΪNone
if rasterlist1 is None:
    print("No raster files found in the directory.")
else:
    # ת��
    for raster in rasterlist1:
        print(raster)
        inRaster = raster
        # ��ԭ�ļ����������һ���ļ���
        out = r"E:\USS\CASA03_DigitalViz\GroupProject\data\temp\temp_points\{}".format(raster)
        arcpy.RasterToPoint_conversion(inRaster, out, "Value")
        print("Change done!")

print("Well done!")
