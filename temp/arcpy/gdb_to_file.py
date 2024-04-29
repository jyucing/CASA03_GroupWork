import arcpy
import os

# ��������ĵ������ݿ�·��
gdb_path = "E:/USS/CASA03_DigitalViz/GroupProject/data/temp/temp_points.gdb"

# ��������ļ���·��
output_folder = "E:/USS/CASA03_DigitalViz/GroupProject/data/temp/temp_points"

# ����ArcGIS��������Ϊ�������ݿ�
arcpy.env.workspace = gdb_path

# �г�����Ҫ����
feature_classes = arcpy.ListFeatureClasses()

# ��������Ҫ���ಢ����ΪShapefile
for fc in feature_classes:
    # �������Shapefile������·��
    output_shapefile = os.path.join(output_folder, "{}.shp".format(fc))
    
    # ����Ҫ����ΪShapefile
    arcpy.FeatureClassToShapefile_conversion(fc, output_folder)
    print("Exported {} to {}".format(fc, output_shapefile))
