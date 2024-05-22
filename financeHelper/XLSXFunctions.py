def cleanSheet(minWeek, sheet):
    valAvail = True
    i = 2
    replaceRow = 2
    while valAvail:
        value = sheet.cell(row=i, column = 1).value

        if value == None:
            valAvail = False
        else:
            if int(sheet.cell(row = i, column = 3).value) >= minWeek:
                if replaceRow == 2:
                    replaceRow = i
                sheet.cell(row = i, column = 1).value = None
                sheet.cell(row = i, column = 2).value = None
                sheet.cell(row = i, column = 3).value = None
                sheet.cell(row = i, column = 4).value = None
        i = i + 1
    
    return replaceRow

def placeValues(replaceRow, sheet, arr):
    for i in range(0, len(arr)):
        ind = i + replaceRow
        elem = arr[i]

        sheet.cell(row = ind, column = 1).value = elem[0]
        sheet.cell(row = ind, column = 2).value = elem[1]
        sheet.cell(row = ind, column = 3).value = elem[2]
        sheet.cell(row = ind, column = 4).value = elem[3]