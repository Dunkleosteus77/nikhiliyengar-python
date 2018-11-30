weekends = {'Jan' : [6,7,13,14,20,21,27,28], 'Feb' : [3,4,10,11,17,18,24,25], 'Mar' : [3,4,10,11,17,18,24,25,31], 'Apr' : [1,7,8,14,15,21,22,28,29], 'May' : [5,6,12,13,19,20,26,27], 'Jun' : [2,3,9,10,16,17,23,24,30], 'Jul' : [1,7,8,14,15,21,22,28,29], 'Aug' : [4,5,11,12,18,19,25,26], 'Sept' : [1,2,8,9,15,16,22,23,29,30], 'Oct' : [6,7,13,14,20,21,27,28], 'Nov' : [3,4,10,11,17,18,24,25], 'Dec' : [1,2,8,9,15,16,22,23,29,30]}
month = input("What month were you born in? ")
day = int(input("What day? "))
if day == weekends[month][0] or day == weekends[month][1] or day == weekends[month][2] or day == weekends[month][3] or day == weekends[month][4] or day == weekends[month][5] or day == weekends[month][6] or day == weekends[month][7] or day == weekends[month][8] or day == weekends[month][9]:
    print("Your birthday's on a weekend this year")
else:
    print("Your birthday's not on a weekend this year")
