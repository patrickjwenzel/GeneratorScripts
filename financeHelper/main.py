import sys
sys.dont_write_bytecode = True
import csv
import os
from CSVFunctions import *
from XLSXFunctions import *
from openpyxl import load_workbook
from datetime import datetime

today = datetime.now()
todayString = today.strftime('%Y%m%d')

csvLocation = os.environ.get('CC_CSV_LOCATION') + todayString + '.csv'

activityFile = open(csvLocation, 'r')
activityReader = csv.reader(activityFile)

cats = {}
places = {}

header = next(activityReader)

total = iterateActivityFile(activityReader, cats, places)
cats = flattenDict(cats, today)
places = flattenDict(places, today)

cats = sorted(cats, key=lambda row: (row[2], row[1]))
places = sorted(places, key=lambda row: (row[2], row[1]))

total = round(total, 2)

if len(sys.argv) == 2 and sys.argv[1] == 'eos':
    cats[-1][3] = 'eos'
    places[-1][3] = 'eos'

printArr(cats)
printArr(places)

xlsxLocation = os.environ.get('CC_XLSX_LOCATION')
wb = load_workbook(xlsxLocation)

catsSheet = wb.worksheets[0]
placesSheet = wb.worksheets[1]

catsRow = cleanSheet(cats[0][2], catsSheet)
placesRow = cleanSheet(places[0][2], placesSheet)

placeValues(catsRow, catsSheet, cats)
placeValues(placesRow, placesSheet, places)

activityFile.close()
wb.save(xlsxLocation)

# GitWorkingFolder/GeneratorScripts/financeHelper