import xlwt


book = xlwt.Workbook()

# add new colour to palette and set RGB colour value
xlwt.add_palette_colour("custom_colour", 0x29)
book.set_colour_RGB(0x29, 255, 0, 0)

# now you can use the colour in styles
sheet1 = book.add_sheet('Sheet 1')
style = xlwt.easyxf('pattern: pattern solid, fore_colour custom_colour')
sheet1.write(0, 0, 'Some text', style)

book.save('test0.xls')
