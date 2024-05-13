from pdfminer.high_level import extract_text
import os

def handle_uploaded_file(f):
    pdfFileObj = open('/Users/mac/Desktop/text_summarize/myProject/media/'+f, 'rb')
    os.remove('/Users/mac/Desktop/text_summarize/myProject/media/'+f) 
    text = extract_text(pdfFileObj)
    return text
    
    