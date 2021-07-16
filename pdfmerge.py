from PyPDF2 import PdfFileWriter, PdfFileReader
import os

def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        print(path)
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    paths = [
    r'D:\sem_3\DELD\practical\TITLE FOR DIGITAL COMMUNICATION JOURNAL.pdf',
    r'D:\sem_3\DELD\practical\U19CS017_DELD_CERTIFICATE_INDEX.pdf',
    r'D:\sem_3\DELD\practical\EXP_1\U19CS017_DELD_EXP-1.pdf',
    r'D:\sem_3\DELD\practical\EXP_2\U19CS017_DELD_EXP-2.pdf',
    r'D:\sem_3\DELD\practical\EXP_3\U19CS017_DELD_EXP-3.pdf',
    r'D:\sem_3\DELD\practical\EXP_3\U19CS017_DLED_EXP-3_ASSIGNMENT.pdf',
    r'D:\sem_3\DELD\practical\EXP_4\U19CS017_DELD_EXP-4.pdf',
    r'D:\sem_3\DELD\practical\EXP_4\U19CS017_DELD_EXP-4_ASSIGNMENT.pdf',
    r'D:\sem_3\DELD\practical\EXP_5\U19CS017_DELD_EXP-5.pdf',
    r'D:\sem_3\DELD\practical\EXP_6\U19CS017_DELD_EXP-6.pdf',
    r'D:\sem_3\DELD\practical\EXP_7\U19CS017_DELD_EXP-7.pdf',
    r'D:\sem_3\DELD\practical\EXP_8&9\U19CS017_DELD_EXP-8.pdf',
    r'D:\sem_3\DELD\practical\EXP_8&9\U19CS017_DELD_EXP-9.pdf',
    r'D:\sem_3\DELD\practical\EXP_10\U19CS017_DELD_EXP-10.pdf',
    r'D:\sem_3\DELD\practical\EXP_11\U19CS017_DELD_EXP-11.pdf',
    r'D:\sem_3\DELD\practical\EXP_12\U19CS017_DELD_EXP-12.pdf',
    r'D:\sem_3\DELD\practical\EXP_13\U19CS017_DELD_EXP-13.pdf',
    ]

    merge_pdfs(paths, output=r'D:\sem_3\DELD\practical\merged.pdf')
