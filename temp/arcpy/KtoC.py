import arcpy

gdb_path = "E:/USS/CASA03_DigitalViz/GroupProject/data/temp/temp_points.gdb"

arcpy.env.workspace = gdb_path

# 列出所有要素类
feature_classes = arcpy.ListFeatureClasses()

# 遍历每个要素类
for fc in feature_classes:
    
    # 检查是否存在`grid_code`字段
    field_names = [field.name for field in arcpy.ListFields(fc)]
    if "grid_code" in field_names:
        # 检查是否需要添加新字段`temp`
        if "temp" not in field_names:
            arcpy.AddField_management(fc, "temp", "DOUBLE")
        
        # 使用UpdateCursor更新字段值
        with arcpy.da.UpdateCursor(fc, ["grid_code", "temp"]) as cursor:
            for row in cursor:
                # 应用数值转换，例如乘以2
                row[1] = row[0] * 0.02 - 273.15
                cursor.updateRow(row)
                
        print("Updated values")
    else:
        print("No 'grid_code' field found")

print("All feature classes processed.")
