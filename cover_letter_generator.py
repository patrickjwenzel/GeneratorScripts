import sys
import os
from docx import Document
from datetime import date

today = date.today()
name = 'Patrick Wenzel'
# Make sure to do \\ instead of \ in your file
TEMPLATE_COVER_LETTER_FOLDER_PATH = "C:\\Users\\patrick.wenzel\\Documents\\Other\\Cover Letter\\"
DOCUMENT_NAME = name + " Cover Letter.docx"
doc = Document(TEMPLATE_COVER_LETTER_FOLDER_PATH + DOCUMENT_NAME)

if len(sys.argv) < 3:
    raise Exception('Not enough arguments provided (company, job, hiring contact name <optional>)')

companyName = sys.argv[1]
jobTitle = sys.argv[2]
hiringContactName = '' if len(sys.argv) < 4 else sys.argv[3]
hiringContactName = 'Hiring Manager' if hiringContactName == '' else hiringContactName

if jobTitle == '':
    raise Exception('Job title not added')
if companyName == '':
    raise Exception('Company name not added')

for paragraph in doc.paragraphs:
    paragraph.text = paragraph.text.replace('[Company Name]', companyName)
    paragraph.text = paragraph.text.replace('[Job Title]', jobTitle)
    paragraph.text = paragraph.text.replace('[Hiring Contact Name]', hiringContactName)
    paragraph.text = paragraph.text.replace('[Current Date]', today.strftime("%d-%b-%Y"))

if not os.path.exists(TEMPLATE_COVER_LETTER_FOLDER_PATH + companyName):
    os.mkdir(TEMPLATE_COVER_LETTER_FOLDER_PATH + companyName)
# Save the document
doc.save(TEMPLATE_COVER_LETTER_FOLDER_PATH + companyName + "\\" + DOCUMENT_NAME)
