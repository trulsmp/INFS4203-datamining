import csv
import dataPreparation as dp

def add_ace_tpw():
    data = dp.get_csv_data("csvFiles/removedEmpty.csv")
    data[0].append('ACE')
    data[0].append('TPW')
    iterrows = iter(data)
    #Skip the header
    next(iterrows)
    for row in iterrows:
        row.append(int(row[5])+int(row[6]))
        row.append(int(row[7])+int(row[8]))
    return data


    # fout = open("tpw_ace_added.csv", "wb")

    # input = open("final.csv", 'rb')
    # writer = csv.writer(fout)
    # reader = csv.reader(input)
    # headerrow = next(reader, None)
    # headerrow.append('ACE')
    # headerrow.append('TPW')
    # writer.writerow(headerrow)
    # for row in reader:
    #     modified_row = row
    #     ACE_value = int(row[5])+int(row[6])
    #     modified_row.append(str(ACE_value))
    #     TPW_value = int(row[7])+int(row[8])
    #     modified_row.append(str(TPW_value))
    #     writer.writerow(row)
    # fout.close()
    # input.close()

def remove_all_but_ace_tpw(readFilename,writeFilename):
    fields = ['ACE','TPW']

    with open(readFilename, 'rb') as infile, open(writeFilename, 'wb') as outfile:
        r = csv.DictReader(infile)
        w = csv.DictWriter(outfile, fields, extrasaction="ignore")
        w.writeheader()
        for row in r:
            w.writerow(row)
def remove_all_but_gender(readFilename,writeFilename):
    fields = ['Gender']

    with open(readFilename, 'rb') as infile, open(writeFilename, 'wb') as outfile:
        r = csv.DictReader(infile)
        w = csv.DictWriter(outfile, fields, extrasaction="ignore")
        w.writeheader()
        for row in r:
            w.writerow(row)

if __name__ == "__main__":
    result = add_ace_tpw()
    dp.write_result("csvFiles/ace_tpw_added.csv", result)
    remove_all_but_ace_tpw("csvFiles/ace_tpw_added.csv", "csvFiles/only_ace_tpw.csv")
    remove_all_but_gender("csvFiles/removedEmpty.csv", "csvFiles/only_gender.csv")
