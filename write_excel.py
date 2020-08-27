# The code allows it to write the top movies into a Excel file


import imdb
import xlsxwriter

row = 1
col = 0

workbook = xlsxwriter.Workbook('Example3.xlsx')
worksheet = workbook.add_worksheet("Top movies")

ia = imdb.IMDb()
top = ia.get_top250_movies()
# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})


# Write some data headers.
worksheet.write('A1', 'Title', bold)
worksheet.write('B1', 'Rating', bold)

# writing the top movies data to excel
# you can change the range value to write how many data
for i in range(10):
    print(top[i]['title'])
    print(top[i]['rating'])
    worksheet.write(row, col, top[i]['title'])
    worksheet.write(row, col + 1, top[i]['rating'])
    row += 1

workbook.close()
