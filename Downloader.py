import requests
import csv
import StringIO

calotteryurl = 'http://www.calottery.com/sitecore/content/Miscellaneous/download-numbers/?GameName=superlotto-plus&Order=Yes'
r = requests.get(calotteryurl)

delminated = r.text.replace('          ', ';').replace('     ', ';').replace('     \r\n', ';')  #build the csv delminters
for i in range(5):  # trim the first 5 lines, nothing of interest
    delminated= delminated[delminated.find('\n')+1:delminated.rfind('\n')]

reader = csv.reader(StringIO.StringIO(delminated),  delimiter=';')

with open('lottery.csv', 'wb') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        outputrow = []
        for col in row:
            #print col
            outputrow.append(col)
        csvwriter.writerow(outputrow)


