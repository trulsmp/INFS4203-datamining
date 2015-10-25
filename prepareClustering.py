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

if __name__ == "__main__":
    result = add_ace_tpw()
    dp.write_result("csvFiles/ace_tpw_added.csv", result)
    fields = ['ACE','TPW']
    dp.remove_fields("csvFiles/ace_tpw_added.csv", "csvFiles/only_ace_tpw.csv", fields)
    fields = ['Gender']
    dp.remove_fields("csvFiles/removedEmpty.csv", "csvFiles/only_gender.csv", fields)
