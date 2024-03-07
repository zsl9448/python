import docx
def open_file(file_path):
    file_path2=(r'%s'%file_path)
    doc = docx.Document(file_path2)
    for paragraph in doc.paragraphs:
        print(paragraph.text)
    print("打开文件:", file_path)
open_file('D:\周松霖\点之记\S205北流隆盛至平旦村二级公路点之记.docx')