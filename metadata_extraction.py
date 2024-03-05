import os
import argparse
import PyPDF2
import docx

def get_pdf_metadata(filepath):
    try:
        with open(filepath,'rb') as pdf_file:
            pdf=PyPDF2.PdfReader(pdf_file)
            info=pdf.metadata
            print("Title:",info.title)
            print("Author:",info.author)
            print("Subject:".info.subject)
            print("Created In:",info.creator)
            print("Creation Date",info.creation_date)
            print("Modification Date:",info.creation_date)
    except Exception as e:
        print("Error",str(e))

def get_docx_metadata(filepath):
    try:
        doc=docx.Document(filepath)
        print("Title:",doc.core_properties.title)
        print("Author:",doc.core_properties.author)
        print("Subject:",doc.core_properties.subject)
        print("Keywords:",doc.core_properties.keywords)
        print("Creation Date",doc.core_properties.created)
        print("Modification Date",doc.core_properties.modified)

    except Exception as e:
        print("Error",str(e))

if __name__=="__main__":
    parser=argparse.ArgumentParser(description="Examine metadata in PDFs and Microsoft word")
    parser.add_argument("filepath",help="Path to the file which is to be examined")
    args=parser.parse_args()

    file_path=args.file_path()
    _,file_extension=os.path.splitext(file_path)

    if file_extension==".pdf":
        get_pdf_metadata(filepath=file_path)
    elif file_extension==".docx":
        get_docx_metadata(filepath=file_path)
    else:
        print("Unsupported file format")
