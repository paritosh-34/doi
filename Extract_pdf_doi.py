import PyPDF2
import re
import os


def pdf_doi(path):
    # Edit according to your path
    # path = os.getcwd()

    # To fetch no of PDF files
    path, dirs, files = next(os.walk(path))
    print(path)
    print(dirs)
    print(files)  # prints the files in directory
    file_count = len(files)
    print(file_count)  # print no. of files

    # Deceleration
    String = "https://d"
    Doilist = []

    for x in range(0, file_count):
        files[x] = path+files[x]
        if files[x].endswith(".pdf"):
            try:
                pdfFileObj = open(files[x], 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                num_pages = pdfReader.numPages
                print("This PDF file is " + files[x])
                for i in range(0, num_pages):
                    PageObj = pdfReader.getPage(i)
                    print("this is page " + str(i + 1))
                    Text = PageObj.extractText()
                    ResSearch = re.search(String, Text)
                    if ResSearch:
                        print(ResSearch.group(0))
                    if ResSearch != None:
                        # print(len(Text))
                        for j in range(0, len(Text)):
                            if Text[j] == "h":
                                toMatch = Text[j] + Text[j + 1] + Text[j + 2] + Text[j + 3] + Text[j + 4] + Text[j + 5] + Text[
                                    j + 6] + Text[j + 7] + Text[j + 8]
                                if toMatch == String:
                                    k = j + 1
                                    link = "h"
                                    while Text[k] != " ":
                                        if Text[k] != "\n":
                                            temp = Text[k]
                                            link = link + temp
                                            k = k + 1
                                        else:
                                            k = k + 1

                                    Doilist.append(link)
                        print(ResSearch)
            except Exception as e:
                print(e)

            print("Length of DOI")
            print(len(Doilist))
            print("DOI link's found in this file :-")
            print(Doilist)
            print(" ")

    return Doilist


if __name__ == '__main__':
    res = pdf_doi('/home/paritosh/PycharmProjects/doi/face recognition/')
    print(res)