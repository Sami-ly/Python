from funcsv import Fun_csv as Fun_csv

file1 = Fun_csv(r"C:\Users\Administrator\Desktop\MyFolder\csv_class\funcsv.csv")
file1.data()
print(file1.data())
print(file1.data_vdf())
print(file1.data_hdf())
print(file1.csv_files_in(r"C:\Users\Administrator\Desktop\MyFolder\csv_class"))
print(file1.creat_and_write())
print(file1.keyword('rahimo'))
print(file1.index_cell('id'))
#file2.clear()

print()

file2 = Fun_csv(r"C:\Users\Administrator\Desktop\MyFolder\csv_class\funcsv_2.csv")
file2.data()
print(file2.data())
print(file2.data_vdf())
print(file2.data_hdf())
print(file2.csv_files_in(r"C:\Users\Administrator\Desktop\MyFolder\csv_class"))
print(file2.creat_and_write())
print(file2.keyword('rahimo'))
print(file2.index_cell('id'))
#file2.clear()

####  what the fuck
# what the fuck