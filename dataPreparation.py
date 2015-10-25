import csv


def get_csv_data(filename):
    csvf = open(filename,'rU')
    rows = csv.reader(csvf)
    csv_data = [row for row in rows]
    csvf.close()
    return csv_data


def write_result(filename,data):
    with open(filename, 'wb') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(data)

def merge_data():
    header = get_csv_data("tennisStats/men1.csv")
    result_data = []
    header[0].append("Gender")
    result_data.append(header[0])

    for num in range(1, 4):
        m = get_csv_data("tennisStats/men"+str(num)+".csv")
        del m[0]
        for i in range(len(m)):
            m[i].append(0)
            result_data.append(m[i])

        w = get_csv_data("tennisStats/women"+str(num)+".csv")
        del w[0]
        for i in range(len(w)):
            w[i].append(1)
            result_data.append(w[i])
    return result_data

def remove_fields(readFilename, writeFilename, fields):
    with open(readFilename) as infile, open(writeFilename, "wb") as outfile:
        r = csv.DictReader(infile)
        w = csv.DictWriter(outfile, fields, extrasaction="ignore")
        w.writeheader()
        for row in r:
            w.writerow(row)

def remove_empty_fields(data):
    result_data = []
    for row in data:
        empty = False
        for field in row:
            if field == '' or field == 'NA':
                empty = True
                break
        if not empty:
            result_data.append(row)
    return result_data

def prepareData():
    result = merge_data()
    write_result("csvFiles/merged.csv", result)

    fields = ["Result", "ST1.1", "ST2.1", "ST1.2", "ST2.2", "ACE.1", "ACE.2", "TPW.1", "TPW.2", "Gender"]
    remove_fields("csvFiles/merged.csv", "csvFiles/headersRemoved.csv", fields)

    headers_removed = get_csv_data("csvFiles/headersRemoved.csv")

    empty_removed = remove_empty_fields(headers_removed)

    write_result("csvFiles/removedEmpty.csv", empty_removed)


if __name__ == "__main__":
    prepareData()


# fout = open("out.csv", "wb")

# with open("tennisStats/men1.csv") as f:
#     header_line = f.readline().strip()
#     header_line = header_line + ',Gender\n'
#     fout.write(header_line)

# for num in range(1, 4):
#     f = open("tennisStats/men"+str(num)+".csv")
#     f.next()  # skip the header
#     for line in f:
#         row_line = line.strip()
#         row_line += ',0\n'
#         fout.write(row_line)
#     f.close()  # not really needed
#     w = open("tennisStats/women"+str(num)+".csv")
#     w.next()  # skip the header
#     for line in w:
#         row_line = line.strip()
#         row_line += ',1\n'
#         fout.write(row_line)
#     w.close()  # not really needed
# fout.close()

# #(Result, ST1.1, ST2.1, ST1.2, ST2.2, ACE.1, ACE.2, TPW.1, TPW.2 and Gender)

# fields = ["Result", "ST1.1", "ST2.1", "ST1.2", "ST2.2", "ACE.1", "ACE.2", "TPW.1", "TPW.2", "Gender"]

# with open("out.csv") as infile, open("removedHeaders.csv", "wb") as outfile:
#     r = csv.DictReader(infile)
#     w = csv.DictWriter(outfile, fields, extrasaction="ignore")
#     w.writeheader()
#     for row in r:
#         w.writerow(row)

# input = open('removedHeaders.csv', 'rb')
# output = open('final.csv', 'wb')
# writer = csv.writer(output)
# for row in csv.reader(input):
#     empty = False
#     for field in row:
#         if field == '' or field == 'NA':
#             empty = True
#             break
#     if not empty:
#         writer.writerow(row)
# input.close()
# output.close()


