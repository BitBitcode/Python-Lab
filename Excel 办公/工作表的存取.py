#-*- coding: utf-8 -*-
# 需要第三方库：xlrd、xlwt（pip安装即可）

# 1、读取某个单元格
# 导入 xlrd 库
import xlrd
#（1）打开工作簿（即Excel文件）
xlsx=xlrd.open_workbook("C:/Users\smile\Documents\GitHub\Python-Lab\Excel 办公\工作簿1.xlsx") # \u 报错！
# （2）打开工作表（即sheet），可以用索引，也可以用名称
table=xlsx.sheet_by_index(0)
#或：table=xlsx.sheet_by_name("sheet1")
r=input("输入行数：")
c=input("输入列数：")
i=int(r)-1
j=int(c)-1
# 注意转换数据类型
# 注意计算机按0行0列开始算
#（3）输出单元格
print("单元格内容为：",table.cell_value(i,j))
print("单元格内容为：",table.cell(i,j).value)
print("单元格内容为：",table.row(i)[j].value)

# 2、写入某个单元格
# 导入 xlwt 库
import xlwt
new_workbook=xlwt.Workbook()
worksheet=new_workbook.add_sheet("new_test") #不写名字就是默认的“sheet1”
worksheet.write(0,0, "test")
new_workbook.save("C:/Users\smile\Documents\GitHub\Python-Lab\Excel 办工\test.xlsx")