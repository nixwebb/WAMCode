__author__ = 'nick'


import csv


def masterReader():
    outFile = open('MasterNick.csv','wb')
    writer = csv.writer(outFile)

    with open('Master.csv', 'rb') as csvfile:
        peopleReader = csv.reader(csvfile)
        for row in peopleReader:
            surname = row[0]
            first = row[1]
            ynBenefit = lookupBenefit(surname,first)
            donationHistory = lookupHistory(surname,first)
            phone = lookupPhone(surname,first)
            row.append(phone)
            row.append(ynBenefit)
            row.append(donationHistory)
            writer.writerow(row)
    outFile.close()


def lookupBenefit(last,first):
    with open('BLAH.csv', 'rb') as csvfile:
        benefitReader = csv.reader(csvfile)
        for row in benefitReader:
            if row[0] == last:
                if row[1] == first:
                    return True
        return False


def lookupPhone(last,first):
    with open('PHONE.csv', 'rb') as csvfile:
        benefitReader = csv.reader(csvfile)
        for row in benefitReader:
            if row[0] == last:
                if row[1] == first:
                    return row[2]
        return "N/A"


def lookupHistory(last,first):
    with open('BLAH.csv', 'rb') as csvfile:
        benefitReader = csv.reader(csvfile)
        for row in benefitReader:
            if row[0] == last:
                if row[1] == first:
                    return row[2:5]
        return []
