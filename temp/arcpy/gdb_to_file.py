import arcpy
import os

# 设置输入的地理数据库路径
gdb_path = "E:/USS/CASA03_DigitalViz/GroupProject/data/temp/temp_points.gdb"

# 设置输出文件夹路径
output_folder = "E:/USS/CASA03_DigitalViz/GroupProject/data/temp/temp_points"

# 设置ArcGIS工作环境为地理数据库
arcpy.env.workspace = gdb_path

# 列出所有要素类
feature_classes = arcpy.ListFeatureClasses()

# 遍历所有要素类并导出为Shapefile
for fc in feature_classes:
    # 定义输出Shapefile的完整路径
    output_shapefile = os.path.join(output_folder, "{}.shp".format(fc))
    
    # 导出要素类为Shapefile
    arcpy.FeatureClassToShapefile_conversion(fc, output_folder)
    print("Exported {} to {}".format(fc, output_shapefile))
