from datetime import datetime

def iterateActivityFile(activityReader, cats, places):
    total = 0

    for row in activityReader:
        amount = round(float(row[5]) * -1, 2)
        total += amount

        cat = row[3]
        place = row[2]
        week = datetime.strptime(row[0], '%m/%d/%Y')
        week = week.strftime('%U')

        if cat not in cats:
            cats[cat] = {
                week: amount
            }
        else:
            if week not in cats[cat]:
                cats[cat][week] = amount
            else :
                cats[cat][week] += amount

        if place not in places:
            places[place] = {
                week: amount
            }
        else:
            if week not in places[place]:
                places[place][week] = amount
            else :
                places[place][week] += amount

        cats[cat][week] = round(cats[cat][week], 2)
        places[place][week] = round(places[place][week], 2)
    
    return total

def flattenDict(dict, today):
    arr = []
    keys = dict.keys()
    week = int(today.strftime('%U'))

    for key in keys:
        weeks = dict[key].keys()
        for week in weeks:
            arr.append([key, dict[key][week], int(week), None])

    return arr

def printArr(arr):
    for elem in arr:
        print(elem)

    print()