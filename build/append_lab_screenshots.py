"""Append source-attributed Microsoft workflow screenshot to each printable lab guide."""
from pathlib import Path
import fitz
from executive_labs import UI_FOR_LAB

ROOT=Path(__file__).resolve().parents[1]
for number,kind in enumerate(UI_FOR_LAB,1):
    folder=ROOT/'labs'/f'lab-{number:02d}'
    pdf_path=folder/'README.pdf'
    doc=fitz.open(pdf_path)
    if any('Workflow reference screenshot' in p.get_text() for p in doc):
        doc.close();continue
    page=doc.new_page(width=595,height=842)
    page.insert_text((44,52),'Workflow reference screenshot',fontsize=17,fontname='helv',color=(.08,.20,.36))
    page.insert_text((44,73),'Official Microsoft Support example for orientation; not evidence of your lab result.',fontsize=9,fontname='helv')
    im_path=folder/'workflow-reference.png'
    pix=fitz.Pixmap(str(im_path))
    width=min(507, pix.width)
    height=width*pix.height/pix.width
    if height>640:height=640;width=height*pix.width/pix.height
    top=100
    rect=fitz.Rect((595-width)/2,top,(595+width)/2,top+height)
    page.insert_image(rect,filename=str(im_path))
    src=(ROOT/'build'/'microsoft-ui'/f'{kind}.source.txt').read_text().strip()
    page.insert_textbox(fitz.Rect(44,top+height+22,551,top+height+90),'Screenshot source: '+src+'\nThe Microsoft interface and available controls may differ in your work account.',fontsize=8,fontname='helv',color=(.25,.30,.36))
    temp=folder/'README.with-image.pdf'
    doc.save(temp,garbage=4,deflate=True);doc.close();temp.replace(pdf_path)
    check=fitz.open(pdf_path)
    assert len(check[-1].get_images())>=1,pdf_path
    check.close()
print('PASS: 10 printable lab guides include attributed Microsoft workflow screenshots')
