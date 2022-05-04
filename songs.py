from prettytable import from_csv
fp = open("pythonsongs2.csv", "r")
mytable = from_csv(fp)
fp.close()
print(mytable.get_string(sortby="Score", reversesort=True))
reversesort = True
