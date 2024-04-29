import arcpy

gdb_path = "E:/USS/CASA03_DigitalViz/GroupProject/data/temp/temp_points.gdb"

arcpy.env.workspace = gdb_path

# �г�����Ҫ����
feature_classes = arcpy.ListFeatureClasses()

# ����ÿ��Ҫ����
for fc in feature_classes:
    
    # ����Ƿ����`grid_code`�ֶ�
    field_names = [field.name for field in arcpy.ListFields(fc)]
    if "grid_code" in field_names:
        # ����Ƿ���Ҫ������ֶ�`temp`
        if "temp" not in field_names:
            arcpy.AddField_management(fc, "temp", "DOUBLE")
        
        # ʹ��UpdateCursor�����ֶ�ֵ
        with arcpy.da.UpdateCursor(fc, ["grid_code", "temp"]) as cursor:
            for row in cursor:
                # Ӧ����ֵת�����������2
                row[1] = row[0] * 0.02 - 273.15
                cursor.updateRow(row)
                
        print("Updated values")
    else:
        print("No 'grid_code' field found")

print("All feature classes processed.")
