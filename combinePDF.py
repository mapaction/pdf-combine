import arcpy, os, string

#Prompt user for output file name

outputFileName = raw_input('Enter Output FileName (include extension xxx.pdf):  ')

#create final pdf

finalPdf = arcpy.mapping.PDFDocumentCreate(os.path.join(os.getcwd(),outputFileName))

#create a list of files in current directory

files_in_dir = os.listdir(os.getcwd())

#loop through list

for file_in_dir in files_in_dir:
    #check if file is a PDF document
    if file_in_dir.endswith('.pdf'):
        #append pdf to final pdf
        finalPdf.appendPages(os.path.join(os.getcwd(),file_in_dir))
