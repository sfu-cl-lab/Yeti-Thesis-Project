import csv

def getData(filename,columnNum):
    csvfile = open('D:/GitHub/Yeti-Thesis-Project/plot/'+filename,'rb')
    data = csv.reader(csvfile)

    for row in data:
            result = [(int)(row[columnNum]) for row in data]
    csvfile.close()

    return result




def getData_String(filename,columnNum):
    csvfile = open('D:/GitHub/Yeti-Thesis-Project/plot/'+filename,'rb')
    data = csv.reader(csvfile)

    for row in data:
            result = [row[columnNum] for row in data]
    csvfile.close()

    return result



def getData_float(filename,columnNum):
    csvfile = open('D:/GitHub/Yeti-Thesis-Project/plot/'+filename,'rb')
    data = csv.reader(csvfile)

    for row in data:
            result = [(float)(row[columnNum]) for row in data]
    csvfile.close()

    return result