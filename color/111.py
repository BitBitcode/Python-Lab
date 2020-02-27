# -*- coding: utf-8 -*-
# 需要第三方库：xlrd、xlwt（pip安装即可）

# 导入 xlrd、xlwt 库
import xlrd
import xlwt

i = 0           # 行 数
j = 0           # 列 数
name_i = 2    # 颜色名称行数
name_j = 1    # 颜色名称列数
RGB_i = i+2     # RGB 颜色行数
Rj = 3        # R 值列数
Gj = 4        # G 值列数
Bj = 5        # B 值列数
# print("单元格内容为：",i,j,Rj,Gj,Bj)

# 打开工作簿（即Excel文件）
xlsx = xlrd.open_workbook("C:\GitHub\color\Beautiful_Color.xlsx")
# 打开工作表（即sheet）
table = xlsx.sheet_by_name("Web_Color")

book = xlwt.Workbook()
sheet1 = book.add_sheet('Sheet 1')

while i < 10:
    name = table.cell_value(name_i, name_j)
    R = int(table.cell_value(RGB_i, Rj))    # 获取 R 值
    G = int(table.cell_value(RGB_i, Gj))    # 获取 G 值
    B = int(table.cell_value(RGB_i, Bj))    # 获取 B 值

    print(name, "：", R, G, B)
    
    RGB_i = RGB_i+1     # 只有行数在变
    name_i = name_i+1   # 只有行数在变

    # add new colour to palette and set RGB colour value
    xlwt.add_palette_colour("custom_colour", 0x21)
    book.set_colour_RGB(0x21, R, G, B)

    # now you can use the colour in styles
    style = xlwt.easyxf('pattern: pattern solid, fore_colour custom_colour')
    sheet1.write(i, j, '完成！', style)
    print("写入", R, G, B)

    i = i+1

book.save('test.xls')
print("完成！")
